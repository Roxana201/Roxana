import cv2
import os

def extract_frames(video_path, output_dir):
    # Verifică dacă folderul de ieșire există, dacă nu, creează-l
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Încarcă fișierul video
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    success = True
    
    while success:
        # Citește cadrul următor
        success, frame = cap.read()
        if success:
            # Salvează cadrul ca imagine
            frame_filename = os.path.join(output_dir, f"frame_{frame_count:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1
    
    cap.release()
    print(f"Extrase {frame_count} cadre și salvate în {output_dir}")

# Specifică calea către fișierul video și folderul de ieșire
video_path = "cale/catre/video.mp4"
output_dir = "cale/catre/folder/imagini"

# Apelează funcția de extragere a cadrelor
extract_frames(video_path, output_dir)
