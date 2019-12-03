from mpu6050 import mpu6050
import time


class TapTyper:
    mpu = mpu6050(0x68)
    acc_threshold = 50
    time_threshold = 7

    def run(self):
        count = 0
        time_elapsed = 0
        is_timer_on = False
        while (True):
            if (is_timer_on):
                curr_time = time.time()
                time_elapsed = curr_time - start_time
                if (time_elapsed > self.time_threshold):
                    print(f'you typed {count}')
                    count = 0
                    is_timer_on = False
            try:
                accel_data = self.mpu.get_accel_data()
                gyro_data = self.mpu.get_gyro_data()
                if (abs(gyro_data['x']) > self.acc_threshold or abs(gyro_data['y']) > self.acc_threshold or abs(gyro_data['z']) > self.acc_threshold):
                    if (is_timer_on):
                        count+=1
                        pass
                    else:
                        start_time = time.time()
                        is_timer_on = True
                        count = 1
                    print(f'tap {count}')
                    time.sleep(0.3)

                #print("Ax:{:.4f}\tAy:{:.4f}\tAz:{:.4f}\tGx:{:.4f}\tGy:{:.4f}\tGz:{:.4f} ".format(accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z']))

            except KeyboardInterrupt:
                break

            time.sleep(0.2)


if __name__ == "__main__":
    program = TapTyper()
    program.run()
