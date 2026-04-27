# hermes sos

### Hermes SOS 技能同步脚本

该脚本用于从远程仓库获取最新的技能组件（Skills）及核心配置文件（SOUL.md），并强制覆盖安装到本地配置目录。

```bash
# 1. 彻底清理可能残留的目录并重新克隆
rm -rf hermes_sos
git clone https://github.com/benx517/hermes_sos.git

# 2. 同步 Smart Home 技能
mkdir -p ~/.hermes/skills/smart-home/
rm -rf ~/.hermes/skills/smart-home/smartthings-cli
cp -r hermes_sos/skills/smartthings-cli ~/.hermes/skills/smart-home/

rm -rf ~/.hermes/skills/smart-home/smartthings-catalog-api
cp -r hermes_sos/skills/smartthings-catalog-api ~/.hermes/skills/smart-home/

# 3. 同步 Productivity 技能 
mkdir -p ~/.hermes/skills/productivity/
rm -rf ~/.hermes/skills/productivity/ocr-and-documents
cp -r hermes_sos/skills/ocr-and-documents ~/.hermes/skills/productivity/

# 4. 同步 SOUL 配置文件
rm -f ~/.hermes/SOUL.md
cp hermes_sos/SOUL.md ~/.hermes/

# 5. 同步 knowledgebase文件
mkdir -p ~/hermes-agent/mydocs/
rm -rf ~/hermes-agent/mydocs/knowledgebase/
cp -r hermes_sos/mydocs/knowledgebase ~/hermes-agent/mydocs/knowledgebase/

echo "Hermes Skills (含 Productivity) 和 SOUL 复制完成！"

```
