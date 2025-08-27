def calculate_total_views(video_views):
    total_views = 0
    
    for views in video_views:
        total_views += views
        
    return total_views

total_video_views = calculate_total_views([1500, 2500, 750, 4200])
print(f"Total views from all videos: {total_video_views}")



def live_stream_monitor():
    viewers = 50
    print(f"Stream is live! Current viewers: {viewers}")

    while viewers > 0:
        change = input("Enter viewer change (+ or - number, e.g., '+5', '-2'), or 'end' to stop the stream: ")

        if change.lower() == 'end':
            print("Stream has been manually ended.")
            break
        
        try:
            viewers += int(change)
            print(f"Viewer count updated. Current viewers: {viewers}")
        except ValueError:
            print("Invalid input. Please enter a number or 'end'.")

    print("Stream has ended due to no viewers.")

# Start the stream monitor.
live_stream_monitor()

