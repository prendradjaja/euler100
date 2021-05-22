import java.lang.Cloneable;
import java.util.ArrayList;
import java.util.Arrays;

// Each chunk is up to 2**15 - 1

public class BigInt implements Cloneable {

  private static int CHUNK_MAX = 0x7FFF;
  private static int RADIX = 0x8000;

  // TODO private
  public ArrayList<Integer> chunks; // Least significant chunk first

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

  // Least significant chunk first
  public String toString() {
    String result = "";
    for (int chunk : chunks) {
      result += String.format("%04X ", chunk);
    }
    return result;
  }
}