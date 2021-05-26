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

  public BigInt mul(BigInt other) {
    // long multiplication with 'this' on bottom

    BigInt[] rows = new BigInt[this.chunks.size()];

    // t,o,r: indices in this.chunks, other.chunks, row.chunks
    for (int t = 0; t < this.chunks.size(); t++) {
      int thisChunk = this.chunks.get(t);
      BigInt row = new BigInt();
      rows[t] = row;

      for (int r = 0; r < t; r++) {
        row.chunks.add(0);
      }

      int carry = 0;
      for (int o = 0; o < other.chunks.size(); o++) {
        int otherChunk = other.chunks.get(o);
        int rowChunk = thisChunk * otherChunk + carry;
        if (rowChunk <= CHUNK_MAX) {
          carry = 0;
        } else {
          carry = rowChunk / RADIX;
          rowChunk = rowChunk % RADIX;
        }
        row.chunks.add(rowChunk);
      }
      row.chunks.add(carry);
    }

    BigInt result = new BigInt();
    for (BigInt row : rows) {
      result = result.add(row);
    }

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

  public static BigInt fromInt(int n) {
    BigInt result = new BigInt();
    result.chunks = new ArrayList<>(Arrays.asList(n));
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
