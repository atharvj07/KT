import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Task954E {

    public static class FastScanner {

        protected DataInputStream dataInputStream;
        protected byte[] buffer = new byte[0x10000];
        protected int bufferOffset;
        protected int bufferLength;
        protected boolean isEndOfFile;

        public FastScanner() throws IOException {
            dataInputStream = new DataInputStream(System.in);
            Read();
        }

        protected void Read() throws IOException {
            final int length = dataInputStream.read(buffer);
            if (length > 0) {
                bufferLength = length;
            } else {
                bufferLength = 0;
                isEndOfFile = true;
            }
            bufferOffset = 0;
        }

        protected byte nextByte() throws IOException {
            if (bufferOffset == bufferLength) {
                if (!isEndOfFile) Read();
                if (isEndOfFile) return 0;
            }
            return buffer[bufferOffset++];
        }

        public int nextInt() throws IOException {
            int a = 0;
            boolean isNegative = false;

            byte b = nextByte();
            while (b <= ' ') b = nextByte();
            if (b == '-') {
                isNegative = true;
                b = nextByte();
            }
            while (b > ' ') {
                a = a * 10 + (b - '0');
                b = nextByte();
            }
            return isNegative ? -a : a;
        }

    }

    public static class Cran implements Comparable {
        public int t;
        public int vmax;

        @Override
        public int compareTo(Object o) {
            return t - ((Cran)o).t;
        }
    }

    public static void main(final String[] args) throws IOException {
        final FastScanner scanner = new FastScanner();
        final int n = scanner.nextInt();
        final int T = scanner.nextInt();

        final Cran[] cranes = new Cran[n];
        for (int i = 0; i < n; i++) cranes[i] = new Cran();

        long sumV = 0;
        long sumVT = 0;
        long sumVEqual = 0;
        boolean isTGreater = false;
        boolean isTLower = false;
        boolean isTEqual = false;

        for (int i = 0; i < n; i++) {
            final int v = scanner.nextInt();
            cranes[i].vmax = v;
            sumV += v;
        }
        for (int i = 0; i < n; i++) {
            final int t = scanner.nextInt();
            cranes[i].t = t;
            if (t > T) isTGreater = true;
            else if (t < T) isTLower = true;
            else {
                isTEqual = true;
                sumVEqual += (long)cranes[i].vmax;
            }
            sumVT += (long)cranes[i].vmax * (long)t;
        }

        if (!isTEqual) {
            if ((isTGreater && !isTLower) || (isTLower && !isTGreater)) {
                // все краны с температурой или меньше или больше заданной - решения нет
                System.out.println(0);
                return;
            }
        }
        if (isTEqual && (!isTGreater || !isTLower)) {
            // есть краны с нужной температурой, а остальные или меньше или больше заданной - решение сумма по равным
            System.out.println(sumVEqual);
            return;
        }
        if (sumVT == (long)T * sumV) {
            // случайно при всех открытых кранах получилась нужная температура
            System.out.println(sumV);
            return;
        }

        Arrays.sort(cranes);

        double t = (double)sumVT / (double)sumV;

        int minPointer = 0;
        int maxPointer = n - 1;

        while (true) {
            if (t > T) {
                // прикручиваем кран с максимальной температурой (снижаем температуру воды)
                // if (cranes[maxPointer].t > T) break;
                double tres = (double)(sumVT - (long)cranes[maxPointer].vmax * (long)cranes[maxPointer].t)
                        / (double)(sumV - (long)cranes[maxPointer].vmax);
                if (tres <= T) {
                    double dV = ((double)T * (double)sumV - (double)sumVT) / ((double)T - (double)cranes[maxPointer].t);
                    System.out.println((double)sumV - dV);
                    return;

                } else {
                    sumV -= (long)cranes[maxPointer].vmax;
                    sumVT -= (long)cranes[maxPointer].vmax * (long)cranes[maxPointer].t;
                    t = tres;
                    maxPointer--;
                }

            } else {

                // прикручиваем кран с минимальной температурой (повышаем температуру воды)
                // if (cranes[minPointer].t < T) break;
                double tres = (double)(sumVT - (long)cranes[minPointer].vmax * (long)cranes[minPointer].t)
                        / (double)(sumV - (long)cranes[minPointer].vmax);
                if (tres >= T) {
                    double dV = ((double)T * (double)sumV - (double)sumVT) / ((double)T - (double)cranes[minPointer].t);
                    System.out.println((double)sumV - dV);
                    return;

                } else {
                    sumV -= (long)cranes[minPointer].vmax;
                    sumVT -= (long)cranes[minPointer].vmax * (long)cranes[minPointer].t;
                    t = tres;
                    minPointer++;
                }

            }
        }
    }

}
