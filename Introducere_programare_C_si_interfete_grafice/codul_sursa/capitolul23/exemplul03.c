#include <gtk/gtk.h>

void end_program (GtkWidget *wid, gpointer ptr)
{
  gtk_main_quit ();
}

static void col_selected (GtkColorChooser *btn, gpointer ptr)
{
  GdkRGBA col;
  gtk_color_chooser_get_rgba (btn, &col);
  printf ("red = %f; green = %f; blue = %f\n", col.red, col.green,
      col.blue);
}

void main (int argc, char *argv[])
{
  gtk_init (&argc, &argv);
  GtkWidget *win = gtk_window_new (GTK_WINDOW_TOPLEVEL);
  GtkWidget *btn = gtk_button_new_with_label ("Close window");
  g_signal_connect (btn, "clicked", G_CALLBACK (end_program),
      NULL);
  g_signal_connect (win, "delete_event", G_CALLBACK (end_program),
      NULL);
  GtkWidget *vbox = gtk_box_new (GTK_ORIENTATION_VERTICAL, 5);
  gtk_container_add (GTK_CONTAINER (win), vbox);
  GtkWidget *col_btn = gtk_color_button_new ();
  g_signal_connect (col_btn, "color-set", G_CALLBACK (col_selected),
      NULL);
  gtk_box_pack_start (GTK_BOX (vbox), col_btn, TRUE, TRUE, 0);
  gtk_box_pack_start (GTK_BOX (vbox), btn, TRUE, TRUE, 0);
  gtk_widget_show_all (win);
  gtk_main ();
}
