import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    // Classe Mapper
    // Legge una riga di testo alla volta e produce coppie (parola, 1)
    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {

        // Valore costante 1 da associare ad ogni parola trovata
        private final static IntWritable one = new IntWritable(1);

        // Oggetto Text riutilizzato per contenere la parola corrente
        private Text word = new Text();

        @Override
        protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            // Converte la riga letta in stringa
            String line = value.toString();

            // Divide la riga in parole usando gli spazi come separatore
            StringTokenizer tokenizer = new StringTokenizer(line);

            // Per ogni parola trovata emette (parola, 1)
            while (tokenizer.hasMoreTokens()) {
                word.set(tokenizer.nextToken());
                context.write(word, one);
            }
        }
    }

    // Classe Reducer
    // Riceve una parola e tutti i valori associati, poi li somma
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

        private IntWritable result = new IntWritable();

        @Override
        protected void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {

            int sum = 0;

            // Somma tutti gli 1 associati alla stessa parola
            for (IntWritable val : values) {
                sum += val.get();
            }

            // Scrive il risultato finale: (parola, totale)
            result.set(sum);
            context.write(key, result);
        }
    }

    // Metodo main: configura ed esegue il job Hadoop
    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");

        // Specifica la classe principale del job
        job.setJarByClass(WordCount.class);

        // Imposta Mapper e Reducer
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(IntSumReducer.class);

        // Tipo di output prodotto dal Reducer
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // File di input e cartella di output
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // Avvia il job e termina il programma
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
