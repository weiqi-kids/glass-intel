# Glass Intel - 玻璃供應鏈情報追蹤

## 專案狀態：初始化完成

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **新聞爬蟲** | 待建立，涵蓋 18 家公司 | 待開發 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | 已設定 |
| **報告生成** | 每日報告、7 日報告 | 待測試 |
| **前端** | Dashboard | 待客製化 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 待設定 |

### 追蹤範圍

#### 公司 (18 家)

**上游 - 原料/纖維** (4 家)
- SCR-Sibelco (矽砂)
- Tata Chemicals 塔塔化工 (純鹼)
- Solvay (化學品)
- Owens Corning (玻璃纖維)

**中游 - 玻璃製造** (10 家)
- Taiwan Glass 台玻, AGC 旭硝子, Nippon Sheet Glass 日本板硝子
- Xinyi Glass 信義玻璃, Xinyi Solar 信義光能, Fuyao Glass 福耀玻璃
- Saint-Gobain 聖戈班, Corning 康寧, O-I Glass, Flat Glass 福萊特

**下游 - 應用** (4 家)
- LONGi Green 隆基綠能 (太陽能)
- First Solar (太陽能)
- AU Optronics 友達 (顯示器)
- Innolux 群創 (顯示器)

**ETFs**: MXI, TAN

#### 主題 (10 個)

- 玻璃價格、光伏玻璃需求、建築活動
- 玻纖電子、汽車玻璃趨勢
- 產能、財報、展望、資本支出、庫存

---

## 標準流程

```
fetch_news → enrich_event → generate_metrics → detect_anomalies →
generate_daily → generate_7d_report → update_baselines → deploy
```

## 快速啟動

```bash
cd repos/glass-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 8000 -d site

# 瀏覽器開啟
open http://localhost:8000
```

## 資料夾結構

```
glass-intel/
├── lib/                        # 規則引擎
├── scripts/                    # 執行腳本
├── configs/                    # 設定檔
│   ├── companies.yml           # 18 家公司 + 上下游關係
│   ├── topics.yml              # 10 個主題 + 關鍵字
│   ├── site.yml                # 網站設定
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   ├── anomaly_rules.yml       # 異常偵測規則
│   └── 7d_highlights_rules.yml # 7 日報告規則
├── fetchers/                   # 公司新聞爬蟲（待建立）
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務數據
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
├── site/
│   ├── index.html              # Dashboard
│   └── data/                   # 前端資料
└── CLAUDE.md
```

## 下一步

1. 建立各公司爬蟲 (`fetchers/*.py`)
2. 測試規則引擎標註
3. 設定 GitHub Actions
4. 客製化前端 Dashboard


---

## 每日例行（進入此 repo 時自動提醒）

當你讀取此 CLAUDE.md 時，主動執行以下檢查並提醒用戶：

### 自動檢查清單

1. **同步最新** — `git pull origin main`
2. **今日 Actions 狀態** — `gh run list --limit 1`
3. **今日事件數** — `wc -l data/events/$(date +%Y-%m-%d).jsonl`
4. **關鍵字審計** — 讀取 `site/data/reports/daily/$(date +%Y-%m-%d).json` 的 `filter_audit` 欄位

### 提醒格式

```
📋 每日狀態
- Actions: ✅/❌
- 今日事件: N 筆
- 關鍵字審計: ✅ 通過 / ⚠️ gate2 擋住率 XX%，建議檢視
```

若 `filter_audit.alert` 為 true 或 `gate2_block_rate > 30%`，提醒用戶：「有關鍵字需要調整，要執行關鍵字審計嗎？」

### 關鍵字審計流程（用戶確認後執行）

1. 檢視 `filter_audit.gate2_samples` 中被擋住的文章標題
2. 判斷每篇是否與本追蹤產業相關
3. 相關的文章 → 找出缺少的關鍵字，建議新增到 `configs/topics.yml`
4. 呈現結果：

```
## 關鍵字審計結果

通過率：XX% | Gate 2 擋住率：XX%

### 被擋住但應通過的文章
| 標題 | 缺少的關鍵字 | 建議加入的主題 |
|------|-------------|--------------|

### 建議新增關鍵字
topics.yml → {topic_id} → keywords 新增：
- keyword1
- keyword2
```

5. 用戶確認後更新 `configs/topics.yml`，commit + push

