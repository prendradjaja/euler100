public class Main {
  public static void main(String[] args) {
    BigInt n = factorial(100);
    int total = 0;
    for (char digit : n.toString().toCharArray()) {
      total += Character.getNumericValue(digit);
    }
    System.out.println(total);
  }

  private static BigInt factorial(int n) {
    BigInt result = BigInt.fromInt(1);
    for (int i = 1; i <= n; i++) {
      result = result.mul(BigInt.fromInt(i));
    }
    return result;
  }
}
