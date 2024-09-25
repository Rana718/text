import os
import yt_dlp as youtube_dl

def download_video_with_quality_choice(url):
    # Function to display available formats without duplicates
    seen_formats = set()
    def list_formats(formats):
        print("\nAvailable video qualities:")
        
        for idx, fmt in enumerate(formats):
            resolution = fmt.get('format_note')
            extension = fmt.get('ext')
            
           
            if resolution in ['storyboard', 'Default', 'low', 'medium']:
                continue
            
            format_tuple = (resolution, extension)
            if format_tuple in seen_formats:
                continue
            
            seen_formats.add(format_tuple)
            if resolution and extension:
                print(f"{len(seen_formats)}. Resolution: {resolution}, Extension: {extension}")

    ydl_opts = {
        'noplaylist': True,
        'quiet': True  
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            
            info_dict = ydl.extract_info(url, download=False)  # Don't download yet
            formats = info_dict.get('formats', [])

            
            list_formats(formats)

            
            choice = int(input("\nEnter the number of the desired quality (e.g., 1, 2, 3...): ")) - 1

            if choice < 0 or choice >= len(seen_formats):
                print("Invalid choice, aborting.")
                return None

            selected_format = formats[choice]['format_id']

            
            ydl_opts = {
                'format': selected_format,
                'outtmpl': '%(title)s.%(ext)s',  # Save in the current working directory
                'noplaylist': True,
                'progress_hooks': [lambda d: print(f"Downloading {d['filename']}") if d['status'] == 'finished' else None],
            }

            # Download the video
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

                # Find the downloaded MP4 file in the current directory
                downloaded_files = [f for f in os.listdir('.') if f.endswith('.mp4')]

                if downloaded_files:
                    video_path = os.path.join(os.getcwd(), downloaded_files[0])
                    print(f"\nDownloaded video saved as: {video_path}")
                    return video_path  # Return the path of the downloaded video
                else:
                    print("No MP4 file found in the current directory.")
                    return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example usage
download_video_with_quality_choice('https://youtu.be/d3n8u3vwGZY?si=e5PFhWULvBxFjBNd')
