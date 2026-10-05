import requests
from datetime import datetime
from collections import Counter

# 模拟的AI热点数据源（实际可替换为RSS或API）
SAMPLE_SOURCES = [
    "https://github.com/trending/ai?since=daily",
    "https://hnrss.org/newest?q=AI",
    "https://www.reddit.com/r/artificial/.rss"
]

# 模拟抓取内容（实际用requests解析）
def fetch_trends():
    # 这里简化为内置关键词列表，实际中会从源获取标题和描述
    mock_articles = [
        "OpenAI releases GPT-5 model",
        "New framework for AI agents",
        "AI in healthcare diagnosis",
        "Open-source LLM training guide",
        "AI ethics debate on bias",
        "GPT-5 vs Claude performance",
        "AI coding assistant tools top list",
        "AI news roundup weekly",
        "Neural network optimization tips",
        "AI and future of work"
    ]
    return mock_articles

def extract_keywords(texts):
    # 简单关键词提取（按空格分词，过滤停用词）
    stopwords = {'a', 'an', 'the', 'of', 'in', 'on', 'for', 'and', 'to', 'vs'}
    words = []
    for text in texts:
        for token in text.lower().split():
            if token not in stopwords and len(token) > 2:
                words.append(token)
    return words

def generate_report(keywords, top_n=5):
    counter = Counter(keywords)
    trending = counter.most_common(top_n)
    lines = []
    lines.append(f"AI趋势日报 - {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("今日热门主题：")
    for i, (word, count) in enumerate(trending, 1):
        lines.append(f"{i}. {word.capitalize()}: {count}次提及")
    lines.append("\n建议关注以上热点，生成深度内容。")
    return "\n".join(lines)

def main():
    # 实际中这里会从sources抓取，但简化用模拟数据
    articles = fetch_trends()
    keywords = extract_keywords(articles)
    report = generate_report(keywords)
    print(report)

if __name__ == "__main__":
    main()
