# Count/Write-frame count-in-video-file
Pass input video in the method 'get_imagearray_with_framelabel' to get image array with the frames labelled on top right corner. (Adjust coordinates as per frame size) Then pass this array to method 'write_frame_video' to convert the image array back to video with a frame counter displayed.
There is an OpenCV method defined as well which you can pass to ensure that the number of frames counted are correct in both methods.
