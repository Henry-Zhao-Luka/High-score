### 调试记录
1. **环境问题**：初次运行提示 `ModuleNotFoundError: No module named 'torch'`。
   **解决**：在虚拟环境中使用 `pip install torch torchvision` 重新安装。
2. **设备映射**：在未配置 CUDA 的环境下运行报错。
   **解决**：增加了 `torch.device` 的逻辑判断，自动切换 CPU/GPU。
3. **数据读取**：MNIST 数据集下载缓慢。
   **解决**：手动挂载代理或通过 torchvision 的 `download=True` 参数多次尝试。
