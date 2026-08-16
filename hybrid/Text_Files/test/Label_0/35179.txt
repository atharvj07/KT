import java.io.*;
import java.math.*;
import java.util.*;
import java.util.stream.*;

@SuppressWarnings("unchecked")
public class P90D {

  abstract class AWidget {
    long width, height;

    public abstract void setBorder(int border);
    public abstract void setSpacing(int spacing);
    public abstract void pack(AWidget widget);
    public abstract long width();
    public abstract long height();
  }

  //----------------------------------------------------------------------------

  class Widget extends AWidget {
    public Widget(int width, int height) {
      this.width = width;
      this.height = height;
    }

    @Override public void setBorder(int border) {;}
    @Override public void setSpacing(int spacing) {;}
    @Override public void pack(AWidget widget) {;}
    
    @Override public long width() {
      return width;
    }

    @Override public long height() {
      return height;
    }
  }

  //----------------------------------------------------------------------------

  abstract class ABox extends AWidget {
    int border, spacing;
    boolean wc = false, hc = false;

    List<AWidget> pack = new ArrayList();

    @Override public void setBorder(int border) {
      this.border = border;
    }

    @Override public void setSpacing(int spacing) {
      this.spacing = spacing;
    }

    @Override public void pack(AWidget widget) {
      pack.add(widget);
    }

    protected long border() {
      return ((pack.size() > 0) ? (border << 1) : 0);
    }

    protected long spacing() {
      return ((pack.size() > 1) ? (spacing * (pack.size() - 1)) : 0);
    }
  }

  //----------------------------------------------------------------------------

  class HBox extends ABox {
    public long width() {
      if (!wc) {
        width = border() + spacing();
        wc = true;
  
        for (AWidget w : pack) {
          width += w.width();
        }
      }

      return width;
    }
    
    public long height() {
      if (!hc) {
        height = 0;
        hc = true;
  
        for (AWidget w : pack) {
          height = Math.max(height, w.height());
        }

        height += border();
      }

      return height;
    }
  }

  //----------------------------------------------------------------------------

  class VBox extends ABox {
    public long width() {
      if (!wc) {
        width = 0;
        wc = true;
        
        for (AWidget w : pack) {
          width = Math.max(width, w.width());
        }

        width += border();
      }

      return width;
    }
    
    public long height() {
      if (!hc) {
        height = border() + spacing();
        hc = true;
  
        for (AWidget w : pack) {
          height += w.height();
        }
      }

      return height;
    }
  }

  //----------------------------------------------------------------------------

  public void run() throws Exception {
    TreeMap<String, AWidget> widgets = new TreeMap();

    for (int n = nextInt(); n > 0; n--) {
      String cmd = nextLine();

      if (cmd.startsWith("Widget ")) {
        String name = cmd.substring(7, cmd.indexOf('('));
        String [] wh = cmd.substring(cmd.indexOf('(') + 1, cmd.indexOf(')')).split(",");
        widgets.put(name, new Widget(Integer.valueOf(wh[0]), Integer.valueOf(wh[1])));
      } else if (cmd.startsWith("HBox ")) {
        String name = cmd.substring(5);
        widgets.put(name, new HBox());
      } else if (cmd.startsWith("VBox ")) {
        String name = cmd.substring(5);
        widgets.put(name, new VBox());
      } else {
        String name = cmd.substring(0, cmd.indexOf('.'));
        cmd = cmd.substring(cmd.indexOf('.') + 1);
        
        if (cmd.startsWith("set_border")) {
          widgets.get(name).setBorder(Integer.valueOf(cmd.substring(11, cmd.indexOf(')'))));
        } else if (cmd.startsWith("set_spacing")) {
          widgets.get(name).setSpacing(Integer.valueOf(cmd.substring(12, cmd.indexOf(')'))));
        } else {
          widgets.get(name).pack(widgets.get(cmd.substring(5, cmd.indexOf(')'))));
        }
      }

    }

    for (Map.Entry<String, AWidget> me : widgets.entrySet()) {
      println(me.getKey() + " " + me.getValue().width() + " " + me.getValue().height());
    }
  }

  public static void main(String... args) throws Exception {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedOutputStream(System.out));
    new P90D().run();
    br.close();
    pw.close();
    System.err.println("\n[Time : " + (System.currentTimeMillis() - startTime) + " ms]");
  }

  static long startTime = System.currentTimeMillis();
  static BufferedReader br;
  static PrintWriter pw;
  StringTokenizer stok;

  String nextToken() throws IOException {
    while (stok == null || !stok.hasMoreTokens()) {
      String s = br.readLine();
      if (s == null) { return null; }
      stok = new StringTokenizer(s);
    }
    return stok.nextToken();
  }

  void print(byte b) { print("" + b); }
  void print(int i) { print("" + i); }
  void print(long l) { print("" + l); }
  void print(double d) { print("" + d); }
  void print(char c) { print("" + c); }
  void print(Object o) {
    if (o instanceof int[]) { print(Arrays.toString((int [])o));
    } else if (o instanceof long[]) { print(Arrays.toString((long [])o));
    } else if (o instanceof char[]) { print(Arrays.toString((char [])o));
    } else if (o instanceof byte[]) { print(Arrays.toString((byte [])o));
    } else if (o instanceof short[]) { print(Arrays.toString((short [])o));
    } else if (o instanceof boolean[]) { print(Arrays.toString((boolean [])o));
    } else if (o instanceof float[]) { print(Arrays.toString((float [])o));
    } else if (o instanceof double[]) { print(Arrays.toString((double [])o));
    } else if (o instanceof Object[]) { print(Arrays.toString((Object [])o));
    } else { print("" + o); }
  }
  void print(String s) { pw.print(s); }
  void println() { println(""); }
  void println(byte b) { println("" + b); }
  void println(int i) { println("" + i); }
  void println(long l) { println("" + l); }
  void println(double d) { println("" + d); }
  void println(char c) { println("" + c); }
  void println(Object o) { print(o); println(); }
  void println(String s) { pw.println(s); }
  int nextInt() throws IOException { return Integer.parseInt(nextToken()); }
  long nextLong() throws IOException { return Long.parseLong(nextToken()); }
  double nextDouble() throws IOException { return Double.parseDouble(nextToken()); }
  char nextChar() throws IOException { return (char) (br.read()); }
  String next() throws IOException { return nextToken(); }
  String nextLine() throws IOException { return br.readLine(); }
  int [] readInt(int size) throws IOException {
    int [] array = new int [size];
    for (int i = 0; i < size; i++) { array[i] = nextInt(); }
    return array;
  }
  long [] readLong(int size) throws IOException {
    long [] array = new long [size];
    for (int i = 0; i < size; i++) { array[i] = nextLong(); }
    return array;
  }
  double [] readDouble(int size) throws IOException {
    double [] array = new double [size];
    for (int i = 0; i < size; i++) { array[i] = nextDouble(); }
    return array;
  }
  String [] readLines(int size) throws IOException {
    String [] array = new String [size];
    for (int i = 0; i < size; i++) { array[i] = nextLine(); }
    return array;
  }
}