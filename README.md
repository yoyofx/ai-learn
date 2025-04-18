# 技术

# Python
* [FastAPI](https://fastapi.tiangolo.com/)

## [langchian](https://python.langchain.com/docs)
 * openai (了解openai 接口和兼容的模型)
 * prompt ( input )
 * output ( sync,stream ) 
 * memory (大语言模型的记忆能力)
 * agent  (规划任务)

## [MCP](https://modelcontextprotocol.io/introduction)
* [server](https://github.com/punkpeye/awesome-mcp-servers) (多语言实现)
* [client](https://github.com/punkpeye/awesome-mcp-clients/) ( SDK Client / ( Cherry Studio /  Claude / Cline) )

## RAG
* 嵌入向量/向量数据库
* 工作流 (自定义规划任务与多 LLM协同完成任务)

# API
## TTS 
* [edge-tts](https://github.com/rany2/edge-tts)
* [Azure TTS](https://azure.microsoft.com/zh-cn/products/ai-services/text-to-speech)
* [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
* [豆包语音合成](https://www.volcengine.com/docs/6561/1257543)

## 语音识别
* [Whisper](https://github.com/openai/whisper)
* [SenseVoice](https://github.com/FunAudioLLM/SenseVoice)
* [snowboy](https://github.com/Kitt-AI/snowboy) (语音唤醒)

## 各大模型接口集成
openai / Claude / ollama / gemini / deepseek / qwen

## 视觉大模型
* [Qwen-VL](https://github.com/QwenLM/Qwen2.5-VL)

# 产品化 
使用系统中创建各种 prompt,知识库,tools等组件组合成一个应用(app)对外部进入对话与输出.
## 基础能力:
* 集成多个大模型接口
* prompt (提示词)
* RAG (知识库)
* tools (MCP)
* agent (自定义工作流)
* 应用对话输入与流式输出
* 语音输入
* 对话语音输出
* 应用暴露API供外部使用
## 高级功能
* 摄像头集成/视觉大模型
* Coding 编码任务
  
