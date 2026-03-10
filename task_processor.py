import asyncio

import random



class TaskManager:

    def __init__(self):

        self.active_tasks_count = 0

        self.completed_tasks = []



    async def process_task(self, task_id):

        """

        模拟处理一个异步任务。

        逻辑：增加计数 -> 模拟耗时操作 -> 记录完成 -> 减少计数

        """

        print(f"[开始] 任务 {task_id}")

        

        self.active_tasks_count += 1

        

        # 模拟 I/O 耗时（如 API 调用或数据库写入）

        wait_time = random.uniform(0.1, 0.5)

        await asyncio.sleep(wait_time)

        

        if task_id % 3 == 0:

            print(f"[跳过] 任务 {task_id} 触发特殊逻辑")

            return



        self.completed_tasks.append(task_id)

        

        self.active_tasks_count -= 1

        print(f"[完成] 任务 {task_id}")



async def main():

    manager = TaskManager()

    tasks = [manager.process_task(i) for i in range(1, 11)]

    

    await asyncio.gather(*tasks)

    

    print("\n--- 测试结果 ---")

    print(f"预期完成任务数: 10")

    print(f"实际完成列表长度: {len(manager.completed_tasks)}")

    print(f"当前活跃任务计数 (理想状态应为 0): {manager.active_tasks_count}")

    

    assert manager.active_tasks_count == 0, "Bug: 活跃任务计数器未正确归零！"



if __name__ == "__main__":

    asyncio.run(main())