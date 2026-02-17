class Captions:
    
    @classmethod
    def convert_temp_to_captions(cls, temp: str, capt_type: str="vtt") -> str:
        # make a blank new captions variable
        current_captions = ""
        if capt_type == "vtt":
            # Required under the VTT standard
            current_captions = "WEBVTT\n\n"
            is_in_segment = False
            is_first = False
            for line in temp.splitlines():
                if line.endswith(":") and not line.startswith("  "):
                    current_captions = current_captions + line.split(":")[0]
                    is_in_segment = True
                    is_first = True
                if line.startswith("  ") and is_in_segment:
                    if is_first:
                        print("first")
                        time = line.split(":")[0].split("/")[0]
                        seconds_left = float(time)
                        minutes = 0
                        hours = 0
                        while True:
                            if seconds_left - 60 <= 0:
                                break
                            else:
                                seconds_left -= 60
                                minutes += 1
                                if minutes - 60 <= 0:
                                    minutes -= 0
                                    hours += 1
                        if len(str(hours)) <= 2:
                            current_captions = current_captions + f"{hours:02}:{minutes:02}:{seconds_left:.3f}"
                        else:
                            current_captions = current_captions + f"{hours}:{minutes:02}:{seconds_left:.3f}"
                        
        return current_captions