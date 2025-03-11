//运行命令：
// 安装依赖：npm install ethers
// node batch_register_metamask_wallets.js

const { ethers } = require("ethers");
const fs = require("fs");

// 需要生成的钱包数量
const numberOfWallets = 2;

function generateWallets(numberOfWallets) {
  const wallets = [];

  for (let i = 0; i < numberOfWallets; i++) {
    const wallet = ethers.Wallet.createRandom();
    wallets.push({
      address: wallet.address,
      privateKey: wallet.privateKey,
    });
  }

  return wallets;
}

function saveWalletsToFile(wallets, filename) {
  // 将钱包数组转换为 JSON 字符串
  const json = JSON.stringify(wallets, null, 2); // 2 代表缩进，以便于阅读
  fs.writeFileSync(filename, json); // 写入文件
  console.log(`钱包信息已保存到 ${filename}`);
}

// 生成钱包并保存
const wallets = generateWallets(numberOfWallets);
saveWalletsToFile(wallets, "wallets.json");