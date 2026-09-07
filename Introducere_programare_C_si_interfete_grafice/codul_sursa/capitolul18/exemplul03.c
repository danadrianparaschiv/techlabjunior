#include <gtk/gtk.h>

GtkWidget *txt;

void end_program (GtkWidget *wid, gpointer ptr)
{
  gtk_main_quit ();
}

void check_toggle (GtkWidget *wid, gpointer ptr)
{
  printf ("The state of the button is %d\n",
      gtk_toggle_button_get_active (GTK_TOGGLE_BUTTON (wid)));
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
  GtkWidget *lbl = gtk_label_new ("My label");
  GtkWidget *chk = gtk_check_button_new_with_label ("My check");
  g_signal_connect (chk, "toggled", G_CALLBACK (check_toggle),
      NULL);
  GtkAdjustment *adj = gtk_adjustment_new (0, -10, 10, 1, 0, 0);
  txt = gtk_spin_button_new (adj, 0, 0);
  GtkWidget *grd = gtk_grid_new ();
  gtk_grid_attach (GTK_GRID (grd), lbl, 0, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), chk, 1, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), btn, 0, 1, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), txt, 1, 1, 1, 1);
  gtk_container_add (GTK_CONTAINER (win), grd);
  gtk_widget_show_all (win);
  gtk_main ();
}
