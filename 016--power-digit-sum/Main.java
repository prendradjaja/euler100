public class Main {
  public static void main(String[] args) {
    BigInt n = BigInt.fromString("2");
    for (int i = 2; i <= 1000; i++) {
      n = n.add(n);
    }

    int total = 0;
    for (char digit : n.toString().toCharArray()) {
      total += Character.getNumericValue(digit);
    }
    System.out.println(total);
  }
}
