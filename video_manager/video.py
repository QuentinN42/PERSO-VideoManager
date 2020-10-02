import cv2


class Video:
    """ Multiple video captures
    
    """
    
    def __init__(self, cams: dict):
        """ Init the Video class
        
        Parameters
        ----------
        cams: dict
            cam_name (str) -> open parameters (with cv2.VideoCapture)
        """
        self.cams = dict()
        for cam_name, params in cams.items():
            try:
                self.cams[cam_name] = cv2.VideoCapture(*params)
            except Exception:
                # TODO(QuentinN42): raise more specific exception
                raise

    def __del__(self):
        for cam in self.cams.values():
            cam.release()
