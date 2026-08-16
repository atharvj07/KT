// This template code suggested by KT BYTE Computer Science Academy
//   for use in reading and writing files for USACO problems.

// https://content.ktbyte.com/problem.java

import java.util.*;
import java.io.*;

public class ExamInBerSU {

    static StreamTokenizer in;

    static int nextInt() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    public static void main(String[] args) throws Exception {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

        int n = nextInt();
        int M = nextInt();

        int[] times = new int[n];

        for (int i = 0; i < n; i++) {
            times[i] = nextInt();
        }

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> used = new PriorityQueue<>();

        long totalTime = 0;
        long savedTime = 0;

        int result = 0;

        for (int i = 0; i < n; i++) {
            int curTime = times[i];

            if (curTime + totalTime <= M) {
                out.print(0);
            }

            else {
                if (used.size() > 0 && used.peek() < priorityQueue.peek()) {
                    int last = used.poll();
                    savedTime -= last;
                    savedTime += priorityQueue.peek();
                    priorityQueue.add(last);
                    used.add(priorityQueue.poll());
                }

                if (curTime + totalTime - savedTime <= M) {
                    while (true) {
                        int last = used.peek();
                        if (curTime + totalTime - (savedTime - last) <= M) {
                            used.poll();
                            priorityQueue.add(last);
                            result--;
                            savedTime -= last;
                        }
                        else {
                            break;
                        }
                    }
                }

                else {
                    while (curTime + totalTime - savedTime > M) {
                        savedTime += priorityQueue.peek();
                        used.add(priorityQueue.poll());
                        result++;
                    }
                }

                out.print(result);
            }

            priorityQueue.add(curTime);
            totalTime += curTime;

            if (i != n-1) out.print(" ");
        }

        out.close();
    }
}


