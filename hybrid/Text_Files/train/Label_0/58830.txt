import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class WaterLily {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in), 32768);
		PrintWriter writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		String[] temp = reader.readLine().split(" ");
		int h = Integer.parseInt(temp[0]);
		int l = Integer.parseInt(temp[1]);
		double depth = (l * 1l * l - h * 1l * h) / 2.0 / h;
		writer.println(String.format("%.15f", depth));
		reader.close();
		writer.close();
	}
}
