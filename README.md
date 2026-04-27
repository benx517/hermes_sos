# hermes sos

### Hermes SOS 技能同步脚本

该脚本用于从远程仓库获取最新的技能组件（Skills）及核心配置文件（SOUL.md），并强制覆盖安装到本地配置目录。

```bash
#!/bin/bash

# 1. 环境准备：克隆远程仓库
# 如果本地已存在该目录，建议先删除或使用 git pull，此处按流程执行克隆
git clone [https://github.com/benx517/hermes_sos.git](https://github.com/benx517/hermes_sos.git)

# 2. 同步 Smart Home 相关技能
# 确保目标父目录存在，避免 cp 命令因路径不存在而失败
mkdir -p ~/.hermes/skills/smart-home/

# [SmartThings CLI] 先清理旧版本，再从仓库复制最新文件
rm -rf ~/.hermes/skills/smart-home/smartthings-cli
cp -r hermes_sos/skills/smartthings-cli ~/.hermes/skills/smart-home/

# [SmartThings Catalog API] 同样执行“先删后拷”的强制覆盖逻辑
rm -rf ~/.hermes/skills/smart-home/smartthings-catalog-api
cp -r hermes_sos/skills/smartthings-catalog-api ~/.hermes/skills/smart-home/

# 3. 同步 Productivity 相关技能
mkdir -p ~/.hermes/skills/productivity/

# [OCR and Documents] 同步文档处理与 OCR 技能模块
rm -rf ~/.hermes/skills/productivity/ocr-and-documents
cp -r hermes_sos/skills/ocr-and-documents ~/.hermes/skills/productivity/

# 4. 同步核心配置文件 (SOUL)
# 更新系统的核心逻辑描述文件 SOUL.md
rm -rf ~/.hermes/SOUL.md
cp hermes_sos/SOUL.md ~/.hermes/

# 5. 清理工作（可选）
# 如果不需要保留克隆的仓库，可以取消下面这一行的注释
# rm -rf hermes_sos

echo "Hermes Skills 和 SOUL 复制完成！"
