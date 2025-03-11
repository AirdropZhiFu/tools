# MetaMask钱包批量生成工具

这个工具用于批量生成MetaMask钱包账户。

## 功能说明

自动批量生成MetaMask钱包账户，并将生成的钱包信息保存为JSON格式。适用于需要管理多个钱包地址的场景。

## 安装依赖

在使用此工具前，请确保已安装所需的依赖：

```bash
npm install
```

## 使用方法

### 基本用法

运行以下命令生成钱包：

```bash
node batch_register_metamask_wallets.js
```

生成的钱包信息将保存在 `wallets.json` 文件中。

### 配置选项

在 `batch_register_metamask_wallets.js` 文件中，你可以修改以下参数：

```javascript
// 要生成的钱包数量
const numberOfWallets = 10;

// 其他配置参数...
```

## 输出文件格式

生成的 `wallets.json` 文件包含以下信息：

```json
[
  {
    "address": "0x...",
    "privateKey": "0x...",
    "mnemonic": "word1 word2 ... word12"
  },
  ...
]
```

## 安全提示

1. 请妥善保管生成的私钥和助记词，不要泄露给他人
2. 建议在离线环境下使用此工具
3. 对于重要资产，建议使用硬件钱包

## 依赖项

本工具使用以下主要依赖：
- ethers.js: 用于生成以太坊钱包
- fs: 用于文件操作 