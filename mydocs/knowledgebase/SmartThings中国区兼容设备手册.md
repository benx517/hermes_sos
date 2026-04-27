# SmartThings 中国区兼容设备全景手册

> 数据来源：Samsung 中国官网 SmartThings 兼容设备 API（`api.samsungiotcloud.cn`）
> 更新日期：2026-04-17
> 总计：14 个大类、140+ 子类、52 个品牌

---

## 一、设备分类总览

### 14 个大类（Super Categories）

| # | 大类名称 | ID | 子类数量 | 说明 |
|---|------|----|------|------|
| 1 | 家用电器 | 1 | 10 | 冰箱、洗衣机、扫地机器人等核心家电 |
| 2 | 智能网关与连接 | 2 | 4 | Hub、桥接器、中继器等基础设施 |
| 3 | 套件 | 3 | 1 | ADT 安全套装等 |
| 4 | 厨房电器 | 4 | 10 | 冰箱、洗碗机、微波炉、烤箱等 |
| 5 | 生活方式与其他 | 5 | 26 | 宠物、EV 充电、车库门等新兴品类 |
| 6 | 照明与能源 | 6 | 0 | 空壳大类，实际子类归入照明和开关/用电 |
| 7 | 个人设备 | 7 | 4 | 手表、手机、平板、耳机 |
| 8 | 传感器与安全 | 8 | 18 | 门锁、摄像头、各类传感器 |
| 9 | 电视与娱乐 | 9 | 9 | 电视、投影机、音响系统 |
| 10 | 用电 | 10 | 3 | 智能插座、能耗监视、恒温器 |
| 11 | 照明和开关 | 11 | 3 | 灯泡、吊灯、开关/调光器 |
| 12 | 空气护理设备 | 12 | 5 | 空调、空气净化器、加湿器、抽湿机 |
| 13 | 可穿戴设备 | 13 | 3 | 手表、智能戒指、耳机 |
| 14 | 健身与健康 | 14 | 4 | 体重秤、健身垫、枕头 |

---

## 二、详细设备能力表

### 2.1 大家电

#### 冰箱（ID: 36）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatCoolingSetpoint` | 设置冷藏/冷冻目标温度 |
| 温度读取 | `temperatureMeasurement` | 读取当前冷藏/冷冻室温度 |
| 门状态 | `contactSensor` / `doorControl` | 门开/关检测 |
| 运行模式 | `custom.thermostatSetpointControl` | 速冷、假日、AI 节能等模式 |
| 功耗报告 | `powerConsumptionReport` | 月度/日度用电量统计 |
| 故障码 | `custom.errorState` | 故障代码查询 |
| 制冰机 | `custom.iceMaker` | 制冰机开关状态 |
| 滤网状态 | `custom.waterFilterStatus` | 净水滤芯剩余寿命 |

#### 洗衣机（ID: 31）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运行状态 | `switch` / `custom.machineState` | 运行/暂停/停止/完成 |
| 洗涤程序 | `custom.dryerOperatingState` | 当前洗涤程序名称 |
| 进度查询 | `custom.washerJobState` | 洗涤阶段（洗涤/漂洗/脱水等） |
| 剩余时间 | `custom.machineState` + `odp` | 剩余完成时间（分钟） |
| 预约功能 | `custom.washerCompletionTime` | 预约洗涤时间设置 |
| 童锁 | `custom.childLock` | 童锁开关状态 |
| 故障码 | `custom.errorState` | 错误代码查询 |

#### 干衣机/烘干机（ID: 44）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运行状态 | `switch` / `custom.dryerOperatingState` | 运行/暂停/完成 |
| 烘干程序 | `custom.dryerOperatingState` | 当前烘干模式 |
| 剩余时间 | `custom.dryerJobState` | 剩余时间 |
| 滤网状态 | `custom.machineState` | 绒毛滤网状态提示 |

#### 衣物护理机 AirDresser（ID: 32）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运行状态 | `switch` | 运行/空闲 |
| 护理程序 | `custom.dryerOperatingState` | 当前护理模式 |
| 剩余时间 | `custom.dryerJobState` | 剩余时间 |

#### 扫地机器人（ID: 48）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开始/暂停清扫 |
| 运行状态 | `custom.robotCleanerCleaningMode` | 清扫/回充/待机 |
| 清扫模式 | `custom.robotCleanerTurboMode` | 强力/标准/静音 |
| 电池电量 | `battery` | 当前电量百分比 |
| 清扫区域 | `custom.robotCleanerMovement` | 指定房间/全屋清扫 |
| 尘盒状态 | `custom.robotCleanerDirtyState` | 尘盒是否需要清理 |
| 故障码 | `custom.errorState` | 错误代码（轮子卡住等） |

#### 洗碗机（ID: 7）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运行状态 | `switch` | 运行/空闲 |
| 洗涤程序 | `custom.dishwasherJobState` | 当前洗涤模式 |
| 剩余时间 | `custom.dishwasherJobState` | 剩余时间 |
| 洗涤剂余量 | `custom.machineState` | 洗涤剂/软水盐余量 |

#### 热水器（ID: 51）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatCoolingSetpoint` | 设定水温 |
| 温度读取 | `temperatureMeasurement` | 当前水温 |
| 运行状态 | `switch` | 加热/待机 |
| 运行模式 | `custom.machineState` | 即热/保温/节能 |

#### 鞋柜（ID: 88）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 杀菌状态 | `switch` | 杀菌功能开关 |
| 运行模式 | `custom.machineState` | 杀菌/烘干/除臭 |

#### 超细纤维过滤器（ID: 82）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 滤网状态 | `custom.waterFilterStatus` | 滤网寿命/更换提醒 |

---

### 2.2 空气护理设备

#### 空调（ID: 38）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatCoolingSetpoint` | 设定温度 |
| 温度读取 | `temperatureMeasurement` | 室内当前温度 |
| 湿度读取 | `relativeHumidityMeasurement` | 室内当前湿度 |
| 开关控制 | `switch` / `airConditionerMode` | 开/关 |
| 运行模式 | `airConditionerMode` | 制冷/制热/除湿/送风/自动 |
| 风速控制 | `custom.airConditionerFanMode` | 自动/低/中/高/ turbo |
| 扫风控制 | `custom.airConditionerOptionalMode` | 上下/左右扫风 |
| Wind-Free | `custom.airConditionerOptionalMode` | 无风感模式开关 |
| 功耗报告 | `powerConsumptionReport` | 用电量统计 |
| 滤网寿命 | `custom.dustFilterAlert` | 滤网清洗提醒 |
| 故障码 | `custom.errorState` | 故障代码查询 |

#### 空气净化器（ID: 43）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 运行模式 | `custom.airConditionerMode` | 自动/睡眠/强力 |
| 空气质量 | `custom.airQualitySensor` | PM2.5/PM10/AQI 指数 |
| 风速控制 | `custom.fanOscillationMode` | 低/中/高 |
| 滤网寿命 | `custom.dustFilterAlert` / `custom.dustFilterStatus` | 滤网剩余百分比 |
| 功耗报告 | `powerConsumptionReport` | 用电量统计 |

#### 加湿器（ID: 18）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 湿度设定 | `custom.thermostatSetpointControl` | 目标湿度 |
| 湿度读取 | `relativeHumidityMeasurement` | 当前室内湿度 |
| 水箱状态 | `custom.machineState` | 水箱水量检测 |
| 运行模式 | `custom.fanOscillationMode` | 自动/睡眠/手动 |

#### 抽湿机/除湿机（ID: 75）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 湿度设定 | `custom.thermostatSetpointControl` | 目标湿度 |
| 湿度读取 | `relativeHumidityMeasurement` | 当前室内湿度 |
| 水箱状态 | `custom.machineState` | 水箱已满提醒 |
| 运行模式 | `custom.airConditionerMode` | 除湿/干衣/自动 |

#### 通风/换气（ID: 74）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 风速控制 | `fanSpeed` | 低/中/高 |
| 运行模式 | `custom.airConditionerMode` | 换气/循环 |

---

### 2.3 传感器与安全

#### 智能门锁（ID: 34）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 锁状态 | `lock` | 锁定/解锁/已上锁/已解锁 |
| 远程开锁 | `lock` | 远程开/关门 |
| 电池电量 | `battery` | 剩余电量百分比 |
| 低电量报警 | `battery` | 低电量提醒 |
| 开锁记录 | — | 开锁事件日志（需通过 events API） |
| 临时密码 | — | 一次性/限时密码管理 |
| 胁迫报警 | — | 胁迫指纹/密码触发告警 |

#### 摄像头（ID: 25）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 在线状态 | `switch` / `healthCheck` | 在线/离线 |
| 录制状态 | `custom.recording` | 录制中/停止 |
| 移动检测 | `motionSensor` | 检测到运动事件 |
| 实时画面 | — | 通过摄像头自有 App 查看 |
| 双向通话 | — | 通过 ST App 语音 |
| 夜视模式 | — | 自动/手动红外夜视 |

#### 门铃（ID: 8）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 按铃事件 | `button` / `bell` | 门铃被按下事件 |
| 视频通话 | — | 视频对讲 |
| 移动检测 | `motionSensor` | 门前有人移动 |

#### 门窗传感器（ID: 21）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开合状态 | `contactSensor` | 打开/关闭 |
| 电池电量 | `battery` | 剩余电量 |
| 开合历史 | — | 通过 events API 查询 |

#### 动作感应器/人体传感器（ID: 39）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运动检测 | `motionSensor` | 检测到/未检测到 |
| 电池电量 | `battery` | 剩余电量 |
| 照度检测 | `illuminanceMeasurement` | 环境光照度（部分型号） |

#### 烟雾探测器（ID: 33）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 烟雾检测 | `smokeDetector` | 检测到烟雾/正常/测试 |
| 电池电量 | `battery` | 剩余电量 |
| 报警状态 | `alarm` | 警报触发 |

#### 温湿度传感器（ID: 124）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度读取 | `temperatureMeasurement` | 当前温度 |
| 湿度读取 | `relativeHumidityMeasurement` | 当前湿度 |
| 电池电量 | `battery` | 剩余电量 |

#### 空气质量传感器（ID: 12）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| PM2.5 | `custom.fineDustSensor` | PM2.5 浓度 |
| PM10 | `custom.veryFineDustSensor` | PM10 浓度 |
| VOC | `custom.vocSensor` | 挥发性有机物浓度 |

#### 光照传感器（ID: 63）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 照度读取 | `illuminanceMeasurement` | 当前光照度（lux） |
| 电池电量 | `battery` | 剩余电量 |

#### 水浸传感器（ID: 5）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 漏水检测 | `waterSensor` | 干燥/潮湿 |
| 电池电量 | `battery` | 剩余电量 |

#### 结冰探测器（ID: 113）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 结冰检测 | `custom.machineState` | 检测到结冰/正常 |
| 温度读取 | `temperatureMeasurement` | 当前温度 |

#### 流量传感器（ID: 134）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 流量检测 | `custom.machineState` | 水流量数据 |

#### 视觉传感器（ID: 91）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 视觉检测 | `presenceSensor` | 检测到人/无人 |

#### 定位标签/追踪器（ID: 10）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 位置追踪 | — | 通过 SmartThings Find 定位 |

---

### 2.4 照明和开关

#### 照明/灯泡（ID: 49）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 亮度调节 | `switchLevel` | 1%-100% 亮度 |
| 色温调节 | `colorTemperature` | 2700K-6500K |
| 颜色控制 | `colorControl` | RGB 全彩（彩光灯泡） |
| 功耗报告 | `powerConsumptionReport` | 用电量统计 |

#### 吊灯（ID: 71）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 亮度调节 | `switchLevel` | 亮度百分比 |
| 色温调节 | `colorTemperature` | 冷暖色温 |

#### 开关/调光器（ID: 20）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 亮度调节 | `switchLevel` | 调光百分比 |
| 场景切换 | `button` | 单击/双击/长按触发场景 |
| 能耗监控 | `powerMeter` | 实时功率（部分型号） |

---

### 2.5 电视与娱乐

#### 电视（ID: 41）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` / `samsungimaging` | 开/关 |
| 音量控制 | `audioVolume` | 音量调节/静音 |
| 频道切换 | `tvChannel` | 频道号/频道名 |
| 输入源切换 | `mediaInputSource` | HDMI/TV/AV 等 |
| 播放控制 | `mediaPlayback` | 播放/暂停/停止 |
| 画面设置 | `custom.pictureMode` | 标准/电影/游戏模式 |
| 运行 App | — | 通过 SmartThings 启动电视 App |

#### 投影机（ID: 57）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 输入源 | `mediaInputSource` | HDMI/无线投屏 |
| 音量控制 | `audioVolume` | 音量调节 |

#### 显示器（ID: 47/59）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 输入源 | `mediaInputSource` | 输入源切换 |

#### 扬声器/Soundbar（ID: 29/65/58）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 音量控制 | `audioVolume` | 音量调节 |
| 播放控制 | `mediaPlayback` | 播放/暂停/上/下一曲 |
| 音源切换 | `mediaInputSource` | 蓝牙/Optical/HDMI |
| 音效模式 | `custom.soundMode` | 标准/环绕/低音增强 |

#### AV 接收器（ID: 69）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 音量控制 | `audioVolume` | 音量调节 |
| 输入源 | `mediaInputSource` | 输入源切换 |
| 音效模式 | `custom.soundMode` | 环绕声模式 |

---

### 2.6 厨房电器

#### 微波炉（ID: 83）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 启动/停止 |
| 功率设定 | `custom.machineState` | 微波功率等级 |
| 时间设定 | `custom.machineState` | 定时时间 |
| 运行状态 | `custom.machineState` | 运行/空闲 |

#### 烤箱/焗炉（ID: 17）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatSetpoint` | 设定温度 |
| 温度读取 | `temperatureMeasurement` | 腔体当前温度 |
| 运行模式 | `custom.machineState` | 烘烤/烧烤/解冻等 |
| 运行状态 | `switch` | 运行/空闲 |
| 定时功能 | `custom.machineState` | 定时关机 |

#### 灶具/炉灶（ID: 6/13）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 火力控制 | `switchLevel` | 各灶头火力等级 |
| 开关控制 | `switch` | 开/关 |
| 安全锁 | `custom.childLock` | 童锁 |

#### 抽油烟机（ID: 81）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 风速控制 | `fanSpeed` | 低/中/高/爆炒 |
| 照明控制 | `switch` | 灯开关 |

#### 洗碗机（ID: 7）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 运行状态 | `switch` | 运行/空闲 |
| 洗涤程序 | `custom.dishwasherJobState` | 洗涤模式 |
| 剩余时间 | `custom.dishwasherJobState` | 剩余时间 |

#### 酒窖（ID: 28）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatCoolingSetpoint` | 设定温度 |
| 温度读取 | `temperatureMeasurement` | 当前温度 |
| 湿度读取 | `relativeHumidityMeasurement` | 当前湿度 |

#### 咖啡机（ID: 72）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 启动冲泡 |
| 运行状态 | `switch` | 冲泡中/待机/清洗 |
| 水量设定 | `custom.machineState` | 杯量/浓度 |

#### 电锅/电饭煲（ID: 86）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开始烹饪 |
| 运行模式 | `custom.machineState` | 煮饭/粥/汤/保温 |
| 预约功能 | `custom.machineState` | 预约时间 |
| 剩余时间 | `custom.machineState` | 剩余烹饪时间 |

#### 净水器（ID: 93）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 滤芯状态 | `custom.waterFilterStatus` | 滤芯寿命百分比 |
| 水质检测 | `custom.waterSensor` | 水质状态 |
| 用水量 | `custom.machineState` | 累计过滤水量 |

---

### 2.7 用电管理

#### 智能插座（ID: 52）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 功耗读取 | `powerMeter` | 实时功率（W） |
| 能耗统计 | `powerConsumptionReport` | 累计用电量（kWh） |
| 电压电流 | `powerMeter` | 电压/电流（部分型号） |

#### 能耗监视（ID: 23）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 功耗读取 | `powerMeter` | 实时功率 |
| 能耗统计 | `powerConsumptionReport` | 日/月/年用电量 |
| 电压/电流 | `powerMeter` | 电压/电流/功率因数 |

#### 恒温器（ID: 26）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度设定 | `thermostatSetpoint` | 目标温度 |
| 温度读取 | `temperatureMeasurement` | 当前温度 |
| 运行模式 | `thermostatMode` | 制冷/制热/自动/关闭 |
| 风扇模式 | `thermostatFanMode` | 自动/持续运转 |
| 湿度读取 | `relativeHumidityMeasurement` | 当前湿度 |

---

### 2.8 生活方式与其他

#### 宠物喂食器（ID: 64）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 喂食控制 | `switch` | 立即喂食 |
| 喂食计划 | `custom.machineState` | 定时喂食计划 |
| 余量检测 | `custom.machineState` | 余粮百分比 |
| 喂食记录 | — | 喂食次数记录 |

#### 猫砂盆（ID: 110）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 清理状态 | `custom.machineState` | 需要清理/正常 |
| 使用记录 | — | 使用次数/频率 |
| 自动清理 | `switch` | 启动自动清理 |

#### 电动汽车充电器（ID: 73）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 充电控制 | `switch` | 开始/停止充电 |
| 充电功率 | `powerMeter` | 实时充电功率（kW） |
| 充电量 | `powerConsumptionReport` | 本次/累计充电量 |
| 充电状态 | `custom.machineState` | 充电中/充满/等待/故障 |
| 充电计划 | `custom.machineState` | 谷电时段充电 |

#### 车库门（ID: 3）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 门状态 | `garageDoorControl` | 开启/关闭/正在移动 |
| 开关控制 | `garageDoorControl` | 远程开/关门 |
| 状态检测 | `contactSensor` | 门是否完全关闭 |

#### 保险柜（ID: 87）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 锁状态 | `lock` | 锁定/解锁 |
| 报警检测 | `tamperAlert` | 异常开启报警 |

#### 灌溉（ID: 50）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` / `valve` | 开/关灌溉 |
| 灌溉计划 | `custom.machineState` | 定时/传感器触发 |
| 阀门控制 | `valve` | 各区域阀门开关 |

#### 宠物饮水机（ID: 141）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开关控制 | `switch` | 开/关 |
| 滤芯状态 | `custom.waterFilterStatus` | 滤芯寿命 |
| 水位检测 | `custom.machineState` | 水位状态 |

#### 开窗器（ID: 139）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 开合控制 | `windowShade` | 开启/关闭/暂停 |
| 开合状态 | `windowShade` | 开合百分比 |

#### 植物栽培设备（ID: 136）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 光照控制 | `switch` / `switchLevel` | 植物灯开关/亮度 |
| 水泵控制 | `switch` / `valve` | 自动浇水 |
| 温湿度读取 | `temperatureMeasurement` / `relativeHumidityMeasurement` | 环境温湿度 |

#### 热泵（ID: 137）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatSetpoint` | 目标温度 |
| 运行模式 | `thermostatMode` | 制热/制冷 |
| 运行状态 | `switch` | 运行/待机 |

#### 淋浴器（ID: 127）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 水温控制 | `thermostatSetpoint` | 水温设定 |
| 运行状态 | `switch` | 运行/待机 |

#### 床组/智能床垫（ID: 67）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 角度调节 | `switchLevel` | 床头/床尾角度 |
| 温度调节 | `thermostatSetpoint` | 床垫温度 |
| 睡眠监测 | `presenceSensor` | 是否在床上 |

#### 温热床垫（ID: 80）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatSetpoint` | 设定温度 |
| 运行模式 | `custom.machineState` | 加热/保温/关闭 |

#### 枕头（ID: 130）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 温度控制 | `thermostatSetpoint` | 枕头温度 |
| 硬度调节 | `switchLevel` | 枕头高度/硬度 |

---

### 2.9 智能网关与连接

#### WLAN/集线器 Hub（ID: 4）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 在线状态 | `healthCheck` | Hub 在线/离线 |
| Zigbee 状态 | — | Zigbee 网络状态 |
| Z-Wave 状态 | — | Z-Wave 网络状态 |
| 子设备列表 | — | 连接的子设备 |

#### 桥接器（ID: 66）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 在线状态 | `healthCheck` | 桥接器状态 |
| 子设备同步 | — | 同步子设备状态 |

#### 中继器/扩展器（ID: 85）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 在线状态 | `healthCheck` | 中继器状态 |
| 信号强度 | — | 信号质量 |

#### Smart home adapter（ID: 27）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 在线状态 | `healthCheck` | 适配器状态 |
| 协议转换 | — | Zigbee/Z-Wave/Matter 协议转换 |

---

### 2.10 可穿戴设备

#### 手表（ID: 92）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 健康数据 | — | 心率/步数/睡眠（通过 Samsung Health） |
| 设备状态 | `healthCheck` | 在线状态 |
| 遥控器 | `button` | 作为智能家居遥控器 |

#### 智能戒指（ID: 111）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 健康数据 | — | 睡眠/心率/体温（通过 Samsung Health） |
| 手势控制 | `button` | 手势触发自动化 |

#### 耳机（ID: 78/112）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 电池电量 | `battery` | 左右耳/充电盒电量 |
| 佩戴状态 | `presenceSensor` | 是否佩戴中 |

---

### 2.11 健身与健康

#### 体重秤（ID: 107）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 体重数据 | — | 体重/体脂率/BMI（通过 Samsung Health） |
| 用户识别 | — | 自动识别家庭成员 |

#### 健身垫（ID: 61）
| 能力项 | 能力名 | 说明 |
|------|------|------|
| 压力检测 | — | 动作纠正（通过配套 App） |
| 运动模式 | — | 瑜伽/普拉提模式 |

---

## 三、兼容品牌（52 个）

| 品牌 | 类型 | 主要品类 |
|------|------|------|
| **Samsung** | 三星自有 | 全品类家电、电视、手机 |
| **SmartThings** | 三星自有 | Hub、传感器、虚拟设备 |
| **Samsung Connect** | 三星自有 | 早期 SmartThings 设备 |
| **Aeotec** | 网关/传感器 | SmartThings Hub 硬件版、传感器 |
| **Philips Hue** | 照明 | 灯泡、灯带、桥接器 |
| **Nanoleaf** | 照明 | 智能面板灯、灯带 |
| **Yeelight** | 照明 | 灯泡、吸顶灯、灯带 |
| **Aqara** | 传感器/安防 | 传感器、门锁、开关 |
| **ORVIBO** | 综合 | 传感器、开关、空调控制器 |
| **DOOYA(杜亚)** | 窗帘 | 电动窗帘电机 |
| **HONYAR(鸿雁)** | 电工 | 智能开关、插座 |
| **HEIMAN(海曼)** | 安防 | 烟雾/燃气/水浸传感器 |
| **EZVIZ(萤石)** | 安防 | 摄像头、门铃 |
| **PETKIT** | 宠物 | 喂食器、饮水机、猫砂盆 |
| **Sonos** | 音频 | 智能音箱 |
| **JBL** | 音频 | 智能音箱 |
| **ThirdReality** | 传感器 | 温湿度传感器、开关 |
| **ZEMISMART** | 电工 | 窗帘电机、开关 |
| **Siterwell** | 暖通 | 恒温器、阀门 |
| **GDKES** | 电工 | 智能开关面板 |
| **Wistar** | 电工 | 智能开关 |
| **Onvis** | 传感器 | 温湿度传感器 |
| **i-SENS** | 健康 | 血压计、血糖仪 |
| **MultiIR** | 红外控制 | 万能红外遥控器 |
| **TOTEM** | 照明 | LED 灯带 |
| **BTB** | 综合 | 传感器、开关 |
| **DEEPSMART** | 综合 | 传感器、开关 |
| **Live freely** | 综合 | 智能家居设备 |
| **LSA** | 综合 | 智能家居设备 |
| **xCREAS** | 综合 | 智能家居设备 |
| **SHAWYAR** | 综合 | 智能家居设备 |
| **LENOX FANS** | 风扇 | 智能风扇 |
| **VIVID STORM** | 投影 | 智能投影幕 |
| **Yanmi** | 电工 | 智能开关 |
| **HAOJAI** | 综合 | 智能家居设备 |
| **DuraGreen** | 综合 | 智能家居设备 |
| **JBL** | 音频 | 音响设备 |
| **LeTianPai** | 综合 | 智能家居设备 |
| **Atflee** | 综合 | 智能家居设备 |
| **WALL HERO** | 电工 | 智能面板 |

---

## 四、SmartThings 核心能力（Capabilities）索引

### 通用能力

| 能力名 | 说明 | 适用设备 |
|------|------|------|
| `switch` | 开关控制 | 几乎所有可开关设备 |
| `battery` | 电池电量 | 无线传感器、门锁、遥控器 |
| `healthCheck` | 设备在线状态 | 所有设备 |
| `powerConsumptionReport` | 功耗报告 | 大家电、照明、插座 |
| `refresh` | 刷新设备状态 | 所有设备 |
| `firmwareUpdate` | 固件升级 | 支持 OTA 的设备 |

### 温度与气候

| 能力名 | 说明 | 适用设备 |
|------|------|------|
| `temperatureMeasurement` | 温度读取 | 空调、传感器、冰箱、酒窖 |
| `relativeHumidityMeasurement` | 湿度读取 | 空调、传感器、加湿器、酒窖 |
| `thermostatCoolingSetpoint` | 制冷温度设定 | 空调、冰箱 |
| `thermostatHeatingSetpoint` | 制热温度设定 | 空调、恒温器 |
| `thermostatMode` | 运行模式 | 空调、恒温器 |
| `thermostatFanMode` | 风扇模式 | 空调、恒温器 |

### 传感器

| 能力名 | 说明 | 适用设备 |
|------|------|------|
| `contactSensor` | 开合状态 | 门窗传感器、冰箱门 |
| `motionSensor` | 运动检测 | 人体传感器、摄像头 |
| `smokeDetector` | 烟雾检测 | 烟雾探测器 |
| `waterSensor` | 漏水检测 | 水浸传感器 |
| `illuminanceMeasurement` | 光照度 | 光照传感器 |
| `presenceSensor` | 存在检测 | 人体传感器、床垫 |
| `battery` | 电量 | 所有无线设备 |

### 控制

| 能力名 | 说明 | 适用设备 |
|------|------|------|
| `switchLevel` | 亮度/等级调节 | 灯泡、调光器、风扇 |
| `colorTemperature` | 色温调节 | 智能灯泡 |
| `colorControl` | RGB 颜色控制 | 彩灯灯泡、灯带 |
| `lock` | 门锁控制 | 智能门锁 |
| `garageDoorControl` | 车库门控制 | 车库门控制器 |
| `windowShade` | 窗帘控制 | 窗帘电机、开窗器 |
| `valve` | 阀门控制 | 灌溉阀门 |
| `fanSpeed` | 风速控制 | 空调、净化器、抽油烟机 |

### 媒体

| 能力名 | 说明 | 适用设备 |
|------|------|------|
| `audioVolume` | 音量控制 | 电视、音响 |
| `mediaPlayback` | 播放控制 | 电视、音响 |
| `mediaInputSource` | 输入源切换 | 电视、投影机、音响 |
| `tvChannel` | 频道切换 | 电视 |

---

## 五、注意事项

### 5.1 中国区 vs 全球区差异

- 中国区 API 端点：`api.samsungiotcloud.cn`
- 全球区 API 端点：`api.smartthings.com`
- 部分设备仅在中国区或全球区可用
- 中国区品牌以三星自有和国产品牌为主（Aqara、Yeelight、DOOYA 等）

### 5.2 设备能力因型号而异

同一品类的不同型号可能支持的能力不同。例如：
- 部分冰箱不支持制冰机能力
- 低端灯泡不支持色温/颜色控制
- 基础版传感器不支持电量报告

### 5.3 部分设备前端页面过滤

官网页面的搜索功能过滤了部分品类（扫地机器人、热水器、空调、空气净化器、通风/换气、声响、坐便器、浴霸），但这只是前端展示过滤，**API 层面这些品类是完全支持的**。

### 5.4 事件查询

设备的操作记录（如门锁开锁记录、传感器触发历史）需要通过 SmartThings Events API 查询，不在设备实时状态中返回。

### 5.5 第三方品牌能力限制

第三方品牌设备（如 Philips Hue、Aqara）的能力由品牌方通过 SmartThings 集成定义，可能与三星自有设备的能力集不同。部分高级功能需要通过品牌自有 App 使用。
