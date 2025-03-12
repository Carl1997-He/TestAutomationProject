import schedule
import time
from scripts.pages.log_monitor import LogMonitor
from scripts.utils.wechat_pusher import WeChatPusher

def job():
    log_monitor = LogMonitor("../logs/app.log")
    errors = log_monitor.extract_errors()
    if errors:
        log_monitor.save_errors(errors, "../logs/errors.txt")
        pusher = WeChatPusher("YOUR_WEBHOOK_URL")
        message = f"今日Error日志:\n{''.join(errors)}"
        pusher.send_message(message)
        print("消息已推送")
    else:
        print("今日无Error日志")

schedule.every().day.at("16:30").do(job)

if __name__ == "__main__":
    print("日志监控已启动...")
    while True:
        schedule.run_pending()
        time.sleep(60)