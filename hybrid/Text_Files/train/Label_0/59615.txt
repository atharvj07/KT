import java.io.*;
import java.util.*;
import static java.lang.Math.*;
import java.math.BigInteger;

public class E {
    public static void main(String[] args) {
        Scanner input = new Scanner();
        StringBuilder output = new StringBuilder();

        char[] s = input.next().toCharArray();
        String tt= input.next();
        char[] t = tt.toCharArray();
        int ones = 0;
        int zeros = 0;
        if (s[0] == '1') {
            for (int i = 0; i < s.length; i++) {
                if (s[i] == '0') {
                    s[i] = '1';
                } else {
                    s[i] = '0';
                }
            }
        }
        for (int i = 0; i < s.length; i++) {
            if (s[i] == '0') {
                zeros++;
            } else {
                ones++;
            }
        }

        HashStructure hs = new HashStructure(tt);
        int count = 0;
        for (int i = 1; i <= t.length; i++) {
            int len0 = i;
            int len1 = t.length - zeros * len0;
            if (len1 % ones != 0) {
                continue;
            }
            len1 /= ones;
            long hash0 = hs.getSubstringHash(0, i);
            int start = i;
            boolean first1 = true;
            long hash1 = 0;
            if (len0 <= 0 || len1 <= 0) {
                continue;
            }
            if (len0 * zeros + len1 * ones != t.length) {
                continue;
            }
            // System.err.println(len0 + " " + len1);
            boolean bad = false;
            for (int j = 1; j < s.length; j++) {
                // System.err.println(s[j]);
                if (s[j] == '0') {
                    if (start + len0 > t.length || hs.getSubstringHash(start, start + len0) != hash0) {
                        bad = true;
                        break;
                    }
                    start += len0;
                } else {
                    if (first1) {
                        if (start + len1 > t.length) {
                            bad = true;
                            break;
                        }
                        hash1 = hs.getSubstringHash(start, start + len1);
                        if (hash1 == hash0) {
                            bad = true;
                            break;
                        }
                        first1 = false;
                    } else {
                        if (start + len1 > t.length || hs.getSubstringHash(start, start + len1) != hash1) {
                            bad = true;
                            break;
                        }
                    }
                    start += len1;
                }
            }
            if (!bad && hash0 != hash1) {
                count++;
                // System.err.println(len0 + " " + len1);
            }
            // System.err.println(hash0 + " " + hash1);
        }

        System.out.println(count);
    }

    private static class Scanner {
        BufferedReader br; StringTokenizer st;
        public Scanner(Reader in) { br = new BufferedReader(in); }
        public Scanner() { this(new InputStreamReader(System.in)); }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try { st = new StringTokenizer(br.readLine());
                } catch (IOException e) { e.printStackTrace(); } }
            return st.nextToken(); }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String readNextLine() {
            String str = "";
            try { str = br.readLine();
            } catch (IOException e) { e.printStackTrace(); }
            return str; }
        int[] readIntArray(int n) {
            int[] a = new int[n];
            for (int idx = 0; idx < n; idx++) { a[idx] = nextInt(); }
            return a; }
        long[] readLongArray(int n) {
            long[] a = new long[n];
            for (int idx = 0; idx < n; idx++) { a[idx] = nextLong(); }
            return a; }
    } // end Scanner

  //Collision probability: 10^-16
  //constructor is O(n)
  //getSubstringHash is O(1)
  public static class HashStructure {
    String str;
    final long chunk_size = 100000000;
    final long prime = 10000000000000061l;
    final long base = 127 + new Random().nextInt(50);
    long[] prefixHashes;
    long[] cachePower;

    public HashStructure(String in) {
      str = in;
      buildPrefixHashes();
      makePowerCache();
    }

    private void buildPrefixHashes() {
      prefixHashes = new long[str.length()+1];
      long hashStart = 0;
      prefixHashes[0] = hashStart;
      for (int a = 0; a < str.length(); a++) {
        hashStart *= base;
        hashStart += str.charAt(a)+1;
        hashStart %= prime;
        prefixHashes[a+1] = hashStart;
      }
    }

    private void makePowerCache(){
      cachePower = new long[str.length()+1];
      long start = 1;
      for(int a = 0; a < str.length()+1; a++){
        cachePower[a] = start;
        start *= base;
        start %= prime;
      }
    }

    //indexing same as string substring
    //start is inclusive
    //end is exclusive
    public long getSubstringHash(int startIdx, int endIdx){
      long fullPrefix = prefixHashes[endIdx];
      long prefix = prefixHashes[startIdx];
      long power = cachePower[endIdx-startIdx];
      long ans = fullPrefix-modular_multiply(prefix, power);
      return ((ans%prime)+prime)%prime;
    }
    //Quickly multiplies two numbers in prime field of 10^16 + 61
    //This can also be done using BigInteger, but this is much faster.
    public long modular_multiply(long op1, long op2){
      long prefix = op1;
      long power = op2;
      long prefixA = prefix%chunk_size;
      long prefixB = prefix/chunk_size;
      long powerA = power%chunk_size;
      long powerB = power/chunk_size;
      long smallChunk = prefixA*powerA;
      long mediumChunk = powerA*prefixB + powerB*prefixA;
      long largeChunk = prefixB*powerB;
      long mediumChunkLeft = mediumChunk/chunk_size;
      long mediumChunkRight = mediumChunk%chunk_size;
      smallChunk += mediumChunkRight*chunk_size;
      largeChunk += mediumChunkLeft;
      smallChunk += largeChunk * -61;
      return smallChunk;
    }

    //Returns a list of hashes of all substrings of length x.
    //Ordered from left to right.
    public ArrayList<Long> getAllXSubstringHashes(int x){
      ArrayList<Long> output = new ArrayList<Long>();
      for(int a = 0; a < str.length()-x+1; a++){
        output.add(getSubstringHash(a, a+x));
      }
      return output;
    }
  }
}
