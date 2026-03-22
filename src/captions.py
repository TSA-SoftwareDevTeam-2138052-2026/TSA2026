class Captions:
    
    @classmethod
    def time_to_timecode(cls, seconds_left: float, sep: str="."):
        minutes = 0
        hours = 0
        while True:
            if seconds_left - 60 <= 0:
                break
            else:
                seconds_left -= 60
                minutes += 1
                if minutes - 60 >= 0:
                    minutes = 0
                    hours += 1
        true_seconds = f"{str(seconds_left).split(".")[0]:{"0"}>2}"
        true_ms = f"{float("0." + str(seconds_left).split(".")[1]):.3f}".split(".")[1]
        if len(str(hours)) <= 2:
            return f"{hours:02}:{minutes:02}:{true_seconds}{sep}{true_ms}"
        else:
            return f"{hours}:{minutes:02}:{true_seconds}{sep}{true_ms}"
        
    @classmethod
    def convert_temp_to_captions(cls, temp: str, capt_type: str="vtt") -> str:
        # make a blank new captions variable
        current_captions = ""
        sep = ","
        if capt_type == "vtt":
            # Required under the VTT standard
            current_captions = "WEBVTT\n\n"
            # in vtt, comma separators get turned to "."
            sep = "."
        is_in_segment = False
        is_first = False
        start_line = ""
        end_line = ""
        word_list = []
        for line in temp.splitlines():
            if line.endswith(":") and not line.startswith("  "):
                if is_in_segment:
                    is_in_segment = False
                    current_captions = current_captions + f"{start_line} --> {end_line}\n{" ".join(word_list)}\n\n"
                    word_list = []
                current_captions = current_captions + str(int(line.split(":")[0]) + 1)  + "\n"
                is_in_segment = True
                is_first = True
                start_line = ""
            elif line.startswith("  ") and is_in_segment:
                if is_first:
                    is_first = False
                    time = line.split(":")[0].split("/")[0]
                    seconds_left = float(time)
                    start_line = cls.time_to_timecode(seconds_left, sep)
                    word_list.append(line.split(": ")[-1])
                else:
                    word_list.append(line.split(": ")[-1])
                    end_line = cls.time_to_timecode(float(line.split(": ")[0].split("/")[1]), sep)
        is_in_segment = False
        current_captions = current_captions + f"{start_line} --> {end_line}\n{" ".join(word_list)}\n"
        word_list = []
        return current_captions