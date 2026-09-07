#include <gtk/gtk.h>

void end_program (GtkWidget *wid, gpointer ptr)
{
  gtk_main_quit ();
}

void combo_changed (GtkWidget *wid, gpointer ptr)
{
  int sel = gtk_combo_box_get_active (GTK_COMBO_BOX (wid));
  printf ("The value of the combo is %d\n", sel);
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
  GtkWidget *rad1 = gtk_radio_button_new_with_label (NULL,
      "Button 1");
  GSList *group = gtk_radio_button_get_group (
      GTK_RADIO_BUTTON (rad1));
  GtkWidget *rad2 = gtk_radio_button_new_with_label (group,
      "Button 2");
  int pos = 0;
  GtkListStore *ls = gtk_list_store_new (1, G_TYPE_STRING);
  gtk_list_store_insert_with_values (ls, NULL, pos++, 0,
      "Option 1", -1);
  gtk_list_store_insert_with_values (ls, NULL, pos++, 0,
      "Option 2", -1);
  gtk_list_store_insert_with_values (ls, NULL, pos++, 0,
      "Option 3", -1);
  GtkWidget *comb = gtk_combo_box_new_with_model (
      GTK_TREE_MODEL (ls));
  GtkCellRenderer *rend = gtk_cell_renderer_text_new ();
  gtk_cell_layout_pack_start (GTK_CELL_LAYOUT (comb), rend, FALSE);
  gtk_cell_layout_add_attribute (GTK_CELL_LAYOUT (comb), rend,
      "text", 0);
  gtk_combo_box_set_active (GTK_COMBO_BOX (comb), 0);
  g_signal_connect (comb, "changed", G_CALLBACK (combo_changed),
      NULL);
  GtkWidget *grd = gtk_grid_new ();
  gtk_grid_attach (GTK_GRID (grd), rad1, 0, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), rad2, 1, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), btn, 0, 1, 1, 1);
  gtk_grid_attach (GTK_GRID (grd), comb, 1, 1, 1, 1);
  gtk_container_add (GTK_CONTAINER (win), grd);
  gtk_widget_show_all (win);
  gtk_main ();
}
