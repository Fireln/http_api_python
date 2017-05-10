import logging
import sys
import setting

class Logging():

    def log_building(self):
        try:
            #set format
            format_str=logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")

            #create stander output handler
            crit_hand=logging.StreamHandler(sys.stderr)
            crit_hand.setFormatter(format_str)

            #create file handler
            file_hand=logging.FileHandler(setting.log["log"],'a')
            file_hand.setFormatter(format_str)

            app_log=logging.getLogger(__name__)
            app_log.addHandler(crit_hand)
            app_log.addHandler(file_hand)

            #设置log输出级别
            app_log.setLevel(logging.INFO)

            return app_log
        except Exception as e:
            logging.shutdown()
            raise e

    def log_level_get(self,level):
        DEBUG_LEVEL={'CRITICAL':logging.CRITICAL,'ERROR':logging.ERROR,'WARNING':logging.WARNING,
                     'INFO':logging.INFO,'DEBUG':logging.DEBUG
            }

        try:
            return DEBUG_LEVEL.get(level.upper())
        except Exception as e:
            raise e

    def write_log(self,level,msg):

        l = self.log_level_get(level)
        log = self.log_building()
        log.log(l,msg)

    def clear_log(self):
        with open(setting.log["log"],'w') as log:
            #log.write('')
            log.close()