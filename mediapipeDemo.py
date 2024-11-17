import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Initialize hands outside of update
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.8, 
            min_tracking_confidence=0.5, 
            max_num_hands=1
        )

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30) 
        self.current_direction = None

    def get_index_finger_direction(self, hand_landmarks):
        tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        pip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP]
        dx = tip.x - pip.x
        dy = tip.y - pip.y

        if abs(dx) > abs(dy):
            return 'RIGHT' if dx > 0 else 'LEFT'
        else:
            return 'DOWN' if dy > 0 else 'UP'

    def update(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)

        # Convert back for display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style())
                direction = self.get_index_finger_direction(hand_landmarks)
                cv2.putText(image, f"Direction: {direction}", (10, 30), 
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                self.current_direction = direction
        
        # Show image and handle key press
        cv2.imshow('MediaPipe Hands', image)
        key = cv2.waitKey(1) 
            
        return self.current_direction

    def cleanup(self):
        try:
            self.hands.close()
            self.cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)  # This additional wait helps ensure windows close
        except Exception as e:
            print(f"Error during cleanup: {e}")
