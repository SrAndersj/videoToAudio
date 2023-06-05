from moviepy.editor import VideoFileClip

def extractAudio(video_filename, output_filename):
    # Cargar el archivo de video
    video = VideoFileClip(video_filename)

    # Extraer el audio del video
    audio = video.audio

    # Guardar el audio como archivo MP3
    audio.write_audiofile(output_filename, codec='mp3')

    # Cerrar los objetos de video y audio
    video.close()
    audio.close()

if __name__ == '__main__':
    video_filename = "/home/srandersj/Vídeos/1videoTest.mp4"
    output_filename = "/home/srandersj/Vídeos/1videoTest.mp3"

    extractAudio(video_filename, output_filename)
