
### 步骤 1：克隆目标仓库到本地
首先，在项目目录下，克隆你想要从主仓库获取代码的GitHub仓库。

```bash
git clone https://github.com/ghowner/ghowner-warehouse.git # 假设仓库名称是ghowner-warehouse
```

### 步骤 2：创建和初始化 submodule

#### 方法一：指定本地分支
如果想在本地直接管理，可以这样做：

1. 创建并切换到本地的主分支：
   ```bash
   git checkout -b master
   ```

2. 初始化 submodule，并指定它追踪该本地分支：
   ```bash
   git submodule init --track ./ghowner-warehouse/master
   ```

#### 方法二：直接从 GitHub 拉取
如果你没有本地的主分支，可以直接拉取并初始化 submodule：

1. 拉取最新的主分支：
   ```bash
   git fetch origin master
   ```

2. 切换到已有的主分支（如果没有的话，可以创建一个）：
     ```bash
     git checkout master
     ```

3. 初始化 submodule，并指定它追踪已拉取的主分支：
     ```bash
     git submodule init --track ./ghowner-warehouse/main
     ```

### 步骤 3：定期更新 submodule

在每次提交代码时，确保 `submodule` 是最新的。操作如下：

4. 拉取最新的代码到本地仓库：
   ```bash
   git fetch origin main
   ```

5. 更新 submodule 的追踪源，并切换回主分支：
   ```bash
   git submodule --track origin/ghowner-warehouse/main
   ```

### 验证和测试

6. **检查 submodule 状态**：
   ```bash
   git status --format="local::%H %h" ./ghowner-warehouse/submodule
   ```

7. **编译项目测试**：
   查看构建结果是否仅使用最新的主分支提交的代码。

### 注意事项

- **权限问题**：确保你有克隆仓库或拉取权限。
- **冲突处理**：如果本地仓库与项目文件存在冲突，需谨慎处理。可能需要删除现有内容后重新克隆或拉取仓库。
- **定期更新**：保持 `submodule` 的最新状态，避免使用过旧的代码。