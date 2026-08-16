// Author : RegalBeast

import java.io.*;
import java.util.*;

public class Main {
  static final FastReader FR = new FastReader();
  static final PrintWriter PW = new PrintWriter(new OutputStreamWriter(System.out));

  public static void main(String[] args) {
    StringBuilder solution = new StringBuilder();
    int rows = FR.nextInt();
    int cols = FR.nextInt();
    int moves = FR.nextInt();

    List<List<Integer>> horizontalEdgeWeights = new ArrayList<List<Integer>>(rows);
    for (int r = 0; r < rows; r++) {
      horizontalEdgeWeights.add(new ArrayList<Integer>(cols-1));

      for (int c = 0; c < cols - 1; c++) {
        horizontalEdgeWeights.get(r).add(FR.nextInt());
      }
    }

    List<List<Integer>> verticalEdgeWeights = new ArrayList<List<Integer>>(rows-1);
    for (int r = 0; r < rows - 1; r++) {
      verticalEdgeWeights.add(new ArrayList<Integer>(cols));

      for (int c = 0; c < cols; c++) {
        verticalEdgeWeights.get(r).add(FR.nextInt());
      }
    }
    
    List<List<Integer>> result = getResult(rows, cols, moves, horizontalEdgeWeights, verticalEdgeWeights);
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        int value = (result != null ? result.get(r).get(c) : -1);
        solution.append(value + " ");
      }
      solution.append("\n");
    }

		PW.print(solution.toString());
    PW.close();
  }

  static List<List<Integer>> getResult(int rows, int cols, int moves, List<List<Integer>> horizontalEdgeWeights, List<List<Integer>> verticalEdgeWeights) {
    if ((moves & 1) == 1) {
      return null;
    }

    int mid = moves >> 1;
    List<List<List<Integer>>> minForDistance = new ArrayList<List<List<Integer>>>(rows);
    for (int r = 0; r < rows; r++) {
      minForDistance.add(new ArrayList<List<Integer>>(cols));

      for (int c = 0; c < cols; c++) {
        minForDistance.get(r).add(new ArrayList<Integer>(Collections.nCopies(mid+1, Integer.MAX_VALUE)));
        minForDistance.get(r).get(c).set(0, 0);
      }
    }

    for (int m = 1; m <= mid; m++) {
      for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
          int minBoredom = minForDistance.get(r).get(c).get(m);

          if (r > 0) {
            if (minForDistance.get(r-1).get(c).get(m-1) < Integer.MAX_VALUE) {
              int candidateBoredom = minForDistance.get(r-1).get(c).get(m-1) + verticalEdgeWeights.get(r-1).get(c);
              minBoredom = Math.min(minBoredom, candidateBoredom);
            }
          }

          if (c > 0) {
            if (minForDistance.get(r).get(c-1).get(m-1) < Integer.MAX_VALUE) {
              int candidateBoredom = minForDistance.get(r).get(c-1).get(m-1) + horizontalEdgeWeights.get(r).get(c-1);
              minBoredom = Math.min(minBoredom, candidateBoredom);
            }
          }
          
          if (r + 1 < rows) {
            if (minForDistance.get(r+1).get(c).get(m-1) < Integer.MAX_VALUE) {
              int candidateBoredom = minForDistance.get(r+1).get(c).get(m-1) + verticalEdgeWeights.get(r).get(c);
              minBoredom = Math.min(minBoredom, candidateBoredom);
            }
          }
   
          if (c + 1 < cols) {
            if (minForDistance.get(r).get(c+1).get(m-1) < Integer.MAX_VALUE) {
              int candidateBoredom = minForDistance.get(r).get(c+1).get(m-1) + horizontalEdgeWeights.get(r).get(c);
              minBoredom = Math.min(minBoredom, candidateBoredom);
            }
          }

          minForDistance.get(r).get(c).set(m, minBoredom);
        }
      }
    }

    List<List<Integer>> result = new ArrayList<List<Integer>>(rows);
    for (int r = 0; r < rows; r++) {
      result.add(new ArrayList<Integer>(cols));

      for (int c = 0; c < cols; c++) {
        result.get(r).add(minForDistance.get(r).get(c).get(mid) << 1);
      }
    }

    return result;
  }

  static class FastReader {
    BufferedReader br;
    StringTokenizer st;

    public FastReader() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
      while (st == null || !st.hasMoreElements()) {
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException  e) {
          e.printStackTrace();
        }
      }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }

    long nextLong() {
      return Long.parseLong(next());
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    String nextLine() {
      String str = "";
      try {
        str = br.readLine();
      } catch (IOException e)  {
        e.printStackTrace();
      }
      return str;
    }
  }
}