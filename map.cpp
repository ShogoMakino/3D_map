#include <iostream>
#include <GL/glut.h>



void mouse(int button, int state, int x, int y){
}

void display(void){
  glClear(GL_COLOR_BUFFER_BIT);
  
}

void resize(int w, int h){
}

void init(){
  glClearColor(1.0, 1.0, 1.0, 1.0);
}

int main(int argc, char* argv[]){
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_RGBA);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(diaplay);
  init();
  glutMainLoop();
  return 0;
}
