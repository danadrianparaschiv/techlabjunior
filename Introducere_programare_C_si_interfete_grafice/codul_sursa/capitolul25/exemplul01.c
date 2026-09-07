#include <gtk/gtk.h>

void main (int argc, char *argv[])
{
  gtk_init (&argc, &argv);
  GtkBuilder *builder = gtk_builder_new_from_file (
        "mylayout.glade");
  GtkWidget *win = (GtkWidget *) gtk_builder_get_object (builder,
      "window1");
  gtk_widget_show_all (win);
  gtk_main ();
}
