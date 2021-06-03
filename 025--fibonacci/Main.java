public class Main {
  public static void main(String[] args) {
    BigInt a = BigInt.fromInt(0);
    BigInt b = BigInt.fromInt(1);
    int bIndex = 1;
    while (b.getDigitCount() < 1000) {
      // System.out.println(bIndex + ": " + b + " = " + b.getDigitCount());
      BigInt c = a.add(b);
      a = b;
      b = c;
      bIndex++;
    }
    System.out.println(bIndex);
  }
}
