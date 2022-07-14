class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log, letter_log=[],[]
        for log in logs:
            second=log.split()[1]
            if second.isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key=lambda x:x.split()[0])
        letter_log.sort(key=lambda x:x.split()[1:])
        return letter_log+digit_log
            
        