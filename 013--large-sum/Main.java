public class Main {
  public static void main(String[] args) {
    BigInt a = new BigInt();
    BigInt b = new BigInt();
    // 95 + 5 = 100
    a.setChunks(new int[]{0x4000, 0x7FFF});
    b.setChunks(new int[]{0x4000,});
    System.out.println(a.add(b));
  }
}