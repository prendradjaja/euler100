import java.lang.Cloneable;
import java.util.ArrayList;
import java.util.Arrays;

public class BigInt implements Cloneable {

  private static int CHUNK_MAX = 9999;
  private static int RADIX = 10_000;
  private static int CHUNK_DIGITS = 4;

  private ArrayList<Integer> chunks; // Least significant chunk first

  public BigInt() {
    chunks = new ArrayList<>();
  }

  public void setChunks(int[] newChunks) {
    chunks = new ArrayList<>(newChunks.length);
    for (int chunk : newChunks) {
      chunks.add(chunk);
    }
  }

  public BigInt clone() {
    BigInt copy = new BigInt();
    copy.chunks = new ArrayList<>(chunks);
    return copy;
  }

  public boolean isValid() {
    for (int chunk : chunks) {
      if (chunk < 0) {
        return false;
      } else if (chunk > CHUNK_MAX) {
        return false;
      }
    }
    return true;
  }

  public BigInt add(BigInt other) {
    BigInt result = new BigInt();
    int length = Math.max(this.chunks.size(), other.chunks.size()) + 1;
    int carry = 0;
    for (int i = 0; i < length; i++) {
      int thisChunk = i < this.chunks.size() ? this.chunks.get(i) : 0;
      int otherChunk = i < other.chunks.size() ? other.chunks.get(i) : 0;
      int resultChunk = thisChunk + otherChunk + carry;
      if (resultChunk <= CHUNK_MAX) {
        carry = 0;
      } else {
        carry = resultChunk / RADIX;
        resultChunk = resultChunk % RADIX;
      }
      result.chunks.add(resultChunk);
    }
    result.trim();
    return result;
  }

  // Remove any unnecessary zero most-significant chunk(s)
  private void trim() {
    for (int i = chunks.size() - 1; i > 0; i--) {
      if (chunks.get(i) == 0) {
        chunks.remove(i);
      } else {
        return;
      }
    }
  }

  // Most significant chunk first
  public String toString() {
    String result = "";
    for (int i = chunks.size() - 1; i >= 0; i--) {
      result += String.format("%04d", chunks.get(i));
    }
    return result;
  }

  public static BigInt fromString(String n) {
    BigInt result = new BigInt();
    int chunkCount = BigInt.getChunkCount(n.length());

    // Pad with zeroes to a whole number of chunks
    int paddingLength = chunkCount * CHUNK_DIGITS - n.length();
    String padding = "";
    for (int i = 0; i < paddingLength; i++) {
      padding += "0";
    }
    n = padding + n;

    // Iterate over chunks from least to most significant
    for (int i = 0; i < chunkCount; i++) {
      int startIndex = (chunkCount - 1 - i) * CHUNK_DIGITS;
      int endIndex = startIndex + 4;
      int chunk = Integer.parseInt(n.substring(startIndex, endIndex));
      result.chunks.add(chunk);
    }

    return result;
  }

  private static int getChunkCount(int digits) {
    return (int) Math.ceil(digits / (float) CHUNK_DIGITS);
  }
}