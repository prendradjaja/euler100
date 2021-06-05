public class Main {
  public static void main(String[] args) {
    BigInt total = BigInt.fromInt(0);
    for (int i = 1; i <= 1000; i++) {
      BigInt partial = BigInt.fromInt(1);
      for (int n = 0; n < i; n++) {
        partial = partial.mul(BigInt.fromInt(i));
      }
      total = total.add(partial);
    }
    String totalString = total.toString();
    System.out.println(totalString.substring(totalString.length() - 10));
  }
}
