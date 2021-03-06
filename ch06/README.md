# 二叉树和树

## 树的重要特征

1. 一个结构如果不为空，则一定有根节点；
2. 一个结点有且只有一个前驱结点，有0个或多个后继结点；
3. 根节点能到达任一结点；
4. 结点之间的联系不会形成循环关系；
5. 从任意两个结点出发构成的后继结点集合，要么不想交，要么一个是另一个的子集。

## 二叉树的性质

1. 在非空二叉树中，第i层最多有2^i个结点(i>=0)；
2. 高度为h的二叉树，最多有2^(h+1) - 1个结点(h>=0)；
3. 非空二叉树，叶子结点数为n0, 度为2的结点数为n2,n0=n2+1；
4. 满二叉树中，叶子结点比分支结点多1；
5. 扩充二叉树的外部路径长度和为E，内部路径长度和为I，内部结点数为n, E = I + 2*n；
6. n个结点的完全二叉树高度为h=floor(log2n)，即不大于log2n的最大整数。
7. 完全二叉树，序号为0的结点为根，i>0,其父结点的编号为(i-1)/2;若2*i+1<n，则2*i+1为其左节点,否则无左子结点；
若2*i+2<n,其右子节点为2*i+2，否则无右子节点。