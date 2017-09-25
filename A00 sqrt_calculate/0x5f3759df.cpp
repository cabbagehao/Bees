// 魔数的来历参考： http://blog.jobbole.com/105295/ 和 https://en.wikipedia.org/wiki/Fast_inverse_square_root
// 和计算机整形和浮点数表示相关而计算出来的一个值。
// 用这个值减去x整形移位后的结果能够就得到一个比较精确的平方根倒数了。
// 然后再用牛顿法精确1次。 效率比c系统函数sqrt还快4倍。

// 此函数计算出的是平方根倒数。
float FastInvSqrt(float x) {
  float xhalf = 0.5f * x;
  int i = *(int*)&x;         // evil floating point bit level hacking
  i = 0x5f3759df - (i >> 1);  // what the fuck?
  x = *(float*)&i;
  x = x*(1.5f-(xhalf*x*x));
  return x;
}
