public class Main {
  public static void main(String[] args) {
    BigInt a = new BigInt();
    BigInt b = new BigInt();
    // 95 + 5 = 100
    a.setChunks(new int[]{5000, 9999});
    b.setChunks(new int[]{5000});
    System.out.println(a.add(b));
  }
}