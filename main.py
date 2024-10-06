import pygetwindow as gw  # Windows 上使用 pygetwindow

# 打印所有窗口标题
def print_all_window_titles():
    all_titles = gw.getAllTitles()
    print("当前所有窗口的标题如下：")
    for title in all_titles:
        print(f"窗口标题: {title}")

# 主函数中调用它，测试窗口标题
if __name__ == "__main__":
    print_all_window_titles()
