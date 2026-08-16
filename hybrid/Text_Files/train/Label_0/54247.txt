import java.util.*;
import java.io.*;
public class E 
{
	
	public static void main(String[] arg) throws IOException
	{
		new E();
	}
	public E() throws IOException
	{
		FastScanner in = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = in.nextInt();
		int k = in.nextInt();
		long[] a = new long[1001];
		for(int i = 0; i < n; i++)
		{
			a[in.nextInt()] = 1;
		}
		a = fastexpo(a, k);
		for(int i = 0; i < a.length; i++)
		{
			if(a[i] > 0) out.print(i + " ");
		}
		in.close(); out.close();
	}
	long[] fastexpo(long[] arr, int exp) {
		if(exp == 1) {
			return arr;
		}
		if(exp%2 == 1)
		{
			long[] ret = fastexpo(arr, exp-1);
			long[] ans = multiply(ret, arr);
			return ans;
		}
		long[] half = fastexpo(arr, exp/2);
		long[] ans = multiply(half, half);
		return ans;
	}
	class FastScanner
	{
		BufferedReader br;
		StringTokenizer st;
		public FastScanner(InputStream in)
		{
			br = new BufferedReader(new InputStreamReader(in));
			st = new StringTokenizer("");
		}
		public String next() throws IOException
		{
			while(!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		public int nextInt() throws IOException
		{
			return Integer.parseInt(next());
		}
		public void close() throws IOException
		{
			br.close();
		}
	}
	void fft(double[] a, double[] b, boolean invert) {
		int count = a.length;
		for (int i = 1, j = 0; i < count; i++) {
			int bit = count >> 1;
			for (; j >= bit; bit >>= 1) j -= bit;
			j += bit;
			if (i < j) {
				double temp = a[i];
				a[i] = a[j];
				a[j] = temp;
				temp = b[i];
				b[i] = b[j];
				b[j] = temp;
			}
		}
		for (int len = 2; len <= count; len <<= 1) {
			int halfLen = len >> 1;
			double angle = 2 * Math.PI / len;
			if (invert) angle = -angle;
			double wLenA = Math.cos(angle), wLenB = Math.sin(angle);
			for (int i = 0; i < count; i += len) {
				double wA = 1, wB = 0;
				for (int j = 0; j < halfLen; j++) {
					double uA = a[i + j], uB = b[i + j];
					double vA = a[i + j + halfLen] * wA - b[i + j + halfLen] * wB;
					double vB = a[i + j + halfLen] * wB + b[i + j + halfLen] * wA;
					a[i + j] = uA + vA;
					b[i + j] = uB + vB;
					a[i + j + halfLen] = uA - vA;
					b[i + j + halfLen] = uB - vB;
					double nextWA = wA * wLenA - wB * wLenB;
					wB = wA * wLenB + wB * wLenA;
					wA = nextWA;
				}
			}
		}
		if (invert) {
			for (int i = 0; i < count; i++) {
				a[i] /= count;
				b[i] /= count;
			}
		}
	}
	long[] multiply(long[] a, long[] b) {
		int resultSize = Integer.highestOneBit(Math.max(a.length, b.length) - 1) << 2;
		resultSize = Math.max(resultSize, 1);
		double[] aReal = new double[resultSize], aImaginary = new double[resultSize];
		double[] bReal = new double[resultSize], bImaginary = new double[resultSize];
		for (int i = 0; i < a.length; i++) aReal[i] = a[i];
		for (int i = 0; i < b.length; i++) bReal[i] = b[i];
		fft(aReal, aImaginary, false);
		if (a == b) 
		{
			System.arraycopy(aReal, 0, bReal, 0, aReal.length);
			System.arraycopy(aImaginary, 0, bImaginary, 0, aImaginary.length);
		} 
		else fft(bReal, bImaginary, false);
		for (int i = 0; i < resultSize; i++) {
			double real = aReal[i] * bReal[i] - aImaginary[i] * bImaginary[i];
			aImaginary[i] = aImaginary[i] * bReal[i] + bImaginary[i] * aReal[i];
			aReal[i] = real;
		}
		fft(aReal, aImaginary, true);
		
		long[] result = new long[Math.min(1_000_001, resultSize)];
		for (int i = 0; i < result.length; i++)
		{
			result[i] = Math.round(aReal[i]) > 0 ? 1 : 0;
		}
		return result;
	}
}