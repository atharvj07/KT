import java.io.BufferedInputStream;
import java.rmi.StubNotFoundException;
import java.util.Collections.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.Writer;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map;
import java.util.Vector;
import java.util.Map.Entry;
import java.util.Queue;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;
import java.math.*;
import java.util.*;
public class Main {
	public static void main(String[]args) throws IOException {
		Scanner scanner=new Scanner(new BufferedInputStream(System.in));
		int n=scanner.nextInt(),t=scanner.nextInt(),c=scanner.nextInt();
		int []a=new int [n]; 
		for (int i=0;i<n;i++)
			a[i]=scanner.nextInt();
		int total=0;
		int temp=0;
		for (int i=0;i<c;i++)
			if (a[i]>t) temp++;

		if (temp==0) total++;
		for (int i=c;i<n;i++){
			if (a[i]>t) temp++;
			if (a[i-c]>t) temp--;
			if (temp==0) total++;
		}
		System.out.println(total);
	}
}
