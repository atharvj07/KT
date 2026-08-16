import java.util.*;

public class Main {
    private static int mod = 200003;

    static class FFT {
        double[] roots;
        int maxN;

        public FFT(int maxN) {
            this.maxN = maxN;
            initRoots();
        }

        public long[] multiply(int[] a, int[] b) {
            int minSize = a.length + b.length - 1;
            int bits = 1;
            while ((1 << bits) < minSize) bits++;
            int N = 1 << bits;
            double[] aa = toComplex(a, N);
            double[] bb = toComplex(b, N);
            fftIterative(aa, false);
            fftIterative(bb, false);
            double[] c = new double[aa.length];
            for (int i = 0; i < N; i++) {
                c[2*i] = aa[2*i]*bb[2*i] - aa[2*i+1]*bb[2*i+1];
                c[2*i+1] = aa[2*i]*bb[2*i+1] + aa[2*i+1]*bb[2*i];
            }
            fftIterative(c, true);
            long[] ret = new long[minSize];
            for (int i = 0; i < ret.length; i++) {
                ret[i] = Math.round(c[2*i]);
            }
            return ret;
        }

        static double[] toComplex(int[] arr, int size) {
            double[] ret = new double[size * 2];
            for (int i = 0; i < arr.length; i++) {
                ret[2*i] = arr[i];
            }
            return ret;
        }

        void initRoots() {
            roots = new double[2 * (maxN + 1)];
            double ang = 2 * Math.PI / maxN;
            for (int i = 0; i <= maxN; i++) {
                roots[2 * i] = Math.cos(i * ang);
                roots[2 * i + 1] = Math.sin(i * ang);
            }
        }

        int bits(int N) {
            int ret = 0;
            while (1 << ret < N) ret++;
            if (1 << ret != N) throw new RuntimeException();
            return ret;
        }

        void fftIterative(double[] array, boolean inv) {
            int bits = bits(array.length / 2);
            int N = 1 << bits;
            for (int from = 0; from < N; from++) {
                int to = Integer.reverse(from) >>> (32 - bits);
                if (from < to) {
                    double tmpR = array[2*from];
                    double tmpI = array[2*from+1];
                    array[2*from] = array[2*to];
                    array[2*from+1] = array[2*to+1];
                    array[2*to] = tmpR;
                    array[2*to+1] = tmpI;
                }
            }
            for (int n = 2; n <= N; n *= 2) {
                int delta = 2 * maxN / n;
                for (int from = 0; from < N; from += n) {
                    int rootIdx = inv ? 2 * maxN : 0;
                    double tmpR, tmpI;
                    for (int arrIdx = 2 * from; arrIdx < 2 * from + n; arrIdx += 2) {
                        tmpR = array[arrIdx + n] * roots[rootIdx] - array[arrIdx + n + 1] * roots[rootIdx + 1];
                        tmpI = array[arrIdx + n] * roots[rootIdx + 1] + array[arrIdx + n + 1] * roots[rootIdx];
                        array[arrIdx + n] = array[arrIdx] - tmpR;
                        array[arrIdx + n + 1] = array[arrIdx + 1] - tmpI;
                        array[arrIdx] += tmpR;
                        array[arrIdx + 1] += tmpI;
                        rootIdx += (inv ? -delta : delta);
                    }
                }
            }
            if (inv) {
                for (int i = 0; i < array.length; i++) {
                    array[i] /= N;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        Map<Integer, Integer> M = new HashMap();
        int[] er = new int[mod];
        er[0] = 1;
        M.put(1, 0);
        for (int i = 1; i < mod - 1; i++) {
            er[i] = er[i - 1] * 2 % mod;
            M.put(er[i], i);
        }
        int[] a = new int[mod - 1];
        for (int i = 0; i < n; i++) {
            int tem = scan.nextInt();
            if (tem > 0) a[M.get(tem)]++;
        }
        int len = 1;
        while (len < 2 * a.length) len *= 2;
        FFT fft = new FFT(len);
        long[] times = fft.multiply(a, a);
        long ans = 0;
        for (int i = 0; i < times.length; i++) {
            ans += er[i % (mod - 1)] * times[i];
        }
        for (int i = 0; i < mod - 1; i++) {
            ans -= er[2 * i % (mod - 1)] * 1L * a[i];
        }
        System.out.println(ans / 2);
    }
}
