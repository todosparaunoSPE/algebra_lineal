# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 16:46:12 2025

@author: jahop
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arrow
import sympy as sp
from PIL import Image
import io

# Configuración de la página
st.set_page_config(
    page_title="Álgebra Lineal Interactiva",
    page_icon="📐",
    layout="wide"
)

# Título y descripción
st.title("📐 Aplicación Interactiva de Álgebra Lineal")
st.markdown("""
**Herramienta educativa para visualizar conceptos fundamentales de álgebra lineal**
""")

# Menú de opciones
opcion = st.sidebar.selectbox(
    "Selecciona un tema:",
    [
        "Vectores y Operaciones",
        "Matrices y Determinantes",
        "Sistemas de Ecuaciones",
        "Transformaciones Lineales",
        "Espacios Vectoriales"
    ]
)

# Sección de Vectores
if opcion == "Vectores y Operaciones":
    st.header("✏️ Vectores y Operaciones Básicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Suma de Vectores")
        x1 = st.slider("Vector 1 - componente x", -10.0, 10.0, 2.0)
        y1 = st.slider("Vector 1 - componente y", -10.0, 10.0, 3.0)
        x2 = st.slider("Vector 2 - componente x", -10.0, 10.0, -1.0)
        y2 = st.slider("Vector 2 - componente y", -10.0, 10.0, 2.0)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='r', label=f'v1 = ({x1}, {y1})')
        ax.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='b', label=f'v2 = ({x2}, {y2})')
        ax.quiver(0, 0, x1+x2, y1+y2, angles='xy', scale_units='xy', scale=1, color='g', label='Suma')
        
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.2)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        ax.set_title("Suma de Vectores en R²")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Producto Punto")
        v1 = np.array([x1, y1])
        v2 = np.array([x2, y2])
        dot_product = np.dot(v1, v2)
        
        st.latex(rf"\vec{{v1}} \cdot \vec{{v2}} = {x1} \times {x2} + {y1} \times {y2} = {dot_product}")
        
        # Cálculo del ángulo
        if np.linalg.norm(v1) > 0 and np.linalg.norm(v2) > 0:
            angle = np.arccos(dot_product / (np.linalg.norm(v1) * np.linalg.norm(v2)))
            angle_deg = np.degrees(angle)
            st.write(f"Ángulo entre vectores: {angle_deg:.2f}°")
            
            # Visualización del ángulo
            fig2, ax2 = plt.subplots(figsize=(6, 6))
            ax2.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='r')
            ax2.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='b')
            
            # Dibujar arco para el ángulo
            radius = 0.5
            ax2.add_patch(plt.Circle((0, 0), radius, color='none', ec='purple', lw=2))
            ax2.text(0.3, 0.1, f"{angle_deg:.1f}°", color='purple', fontsize=12)
            
            ax2.set_xlim(-12, 12)
            ax2.set_ylim(-12, 12)
            ax2.grid(True, linestyle='--', alpha=0.5)
            ax2.set_title("Ángulo entre Vectores")
            st.pyplot(fig2)

# Sección de Matrices
elif opcion == "Matrices y Determinantes":
    st.header("🧮 Matrices y Determinantes")
    
    st.subheader("Calculadora de Matrices")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Matriz A**")
        a11 = st.number_input("a₁₁", value=1.0)
        a12 = st.number_input("a₁₂", value=2.0)
        a21 = st.number_input("a₂₁", value=3.0)
        a22 = st.number_input("a₂₂", value=4.0)
        A = np.array([[a11, a12], [a21, a22]])
        
    with col2:
        st.write("**Matriz B**")
        b11 = st.number_input("b₁₁", value=5.0)
        b12 = st.number_input("b₁₂", value=6.0)
        b21 = st.number_input("b₂₁", value=7.0)
        b22 = st.number_input("b₂₂", value=8.0)
        B = np.array([[b11, b12], [b21, b22]])
    
    operacion = st.selectbox("Operación:", ["Suma", "Resta", "Multiplicación", "Determinante"])
    
    if operacion == "Suma":
        resultado = A + B
        st.latex(f"A + B = {A} + {B} = {resultado}")
    elif operacion == "Resta":
        resultado = A - B
        st.latex(f"A - B = {A} - {B} = {resultado}")
    elif operacion == "Multiplicación":
        resultado = np.dot(A, B)
        st.latex(f"A \times B = {A} \times {B} = {resultado}")
    elif operacion == "Determinante":
        detA = np.linalg.det(A)
        detB = np.linalg.det(B)
        st.latex(f"det(A) = {detA:.2f}")
        st.latex(f"det(B) = {detB:.2f}")
        
        # Visualización del determinante como área
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Para matriz A
        ax.quiver(0, 0, A[0,0], A[1,0], angles='xy', scale_units='xy', scale=1, color='r', label=f'Columna 1 (Área={abs(detA):.2f})')
        ax.quiver(0, 0, A[0,1], A[1,1], angles='xy', scale_units='xy', scale=1, color='b', label='Columna 2')
        
        # Dibujar el paralelogramo
        ax.plot([A[0,0], A[0,0]+A[0,1]], [A[1,0], A[1,0]+A[1,1]], 'k--')
        ax.plot([A[0,1], A[0,0]+A[0,1]], [A[1,1], A[1,0]+A[1,1]], 'k--')
        
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.2)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        ax.set_title("Interpretación Geométrica del Determinante")
        st.pyplot(fig)

# Sección de Sistemas de Ecuaciones
elif opcion == "Sistemas de Ecuaciones":
    st.header("💢 Sistemas de Ecuaciones Lineales")
    
    st.subheader("Resolver sistema 2x2")
    st.write("Ingresa los coeficientes del sistema:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("a (coeficiente de x en ec. 1)", value=2.0)
        b = st.number_input("b (coeficiente de y en ec. 1)", value=3.0)
        c = st.number_input("c (término independiente ec. 1)", value=5.0)
    
    with col2:
        d = st.number_input("d (coeficiente de x en ec. 2)", value=1.0)
        e = st.number_input("e (coeficiente de y en ec. 2)", value=-4.0)
        f = st.number_input("f (término independiente ec. 2)", value=2.0)
    
    # Mostrar el sistema de ecuaciones
    st.latex(f"""
    \\begin{{cases}}
    {a}x + {b}y = {c} \\\\
    {d}x + {e}y = {f}
    \\end{{cases}}
    """)
    
    # Resolver el sistema
    A = np.array([[a, b], [d, e]])
    B = np.array([c, f])
    
    try:
        solucion = np.linalg.solve(A, B)
        st.success(f"Solución: x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
        
        # Visualización gráfica
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Ecuación 1: a*x + b*y = c => y = (c - a*x)/b
        x_vals = np.linspace(-10, 10, 400)
        y1 = (c - a * x_vals) / b
        ax.plot(x_vals, y1, label=f'{a}x + {b}y = {c}')
        
        # Ecuación 2: d*x + e*y = f => y = (f - d*x)/e
        y2 = (f - d * x_vals) / e
        ax.plot(x_vals, y2, label=f'{d}x + {e}y = {f}')
        
        # Punto de solución
        ax.plot(solucion[0], solucion[1], 'ro', label=f'Solución ({solucion[0]:.2f}, {solucion[1]:.2f})')
        
        ax.set_xlim(min(x_vals), max(x_vals))
        ax.set_ylim(-10, 10)
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.2)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        ax.set_title("Representación Gráfica del Sistema")
        st.pyplot(fig)
        
    except np.linalg.LinAlgError:
        st.error("El sistema no tiene solución única (puede ser incompatible o tener infinitas soluciones)")

# Sección de Transformaciones Lineales
elif opcion == "Transformaciones Lineales":
    st.header("🔄 Transformaciones Lineales")
    
    st.subheader("Aplicar transformación a un vector")
    
    # Seleccionar tipo de transformación
    transformacion = st.selectbox(
        "Tipo de transformación:",
        ["Rotación", "Escalamiento", "Cizallamiento", "Reflexión", "Personalizada"]
    )
    
    # Parámetros de la transformación
    if transformacion == "Rotación":
        theta = st.slider("Ángulo de rotación (grados)", -180, 180, 45)
        theta_rad = np.radians(theta)
        T = np.array([
            [np.cos(theta_rad), -np.sin(theta_rad)],
            [np.sin(theta_rad), np.cos(theta_rad)]
        ])
    elif transformacion == "Escalamiento":
        sx = st.slider("Factor de escala en x", 0.1, 3.0, 1.5)
        sy = st.slider("Factor de escala en y", 0.1, 3.0, 0.8)
        T = np.array([
            [sx, 0],
            [0, sy]
        ])
    elif transformacion == "Cizallamiento":
        kx = st.slider("Factor de cizallamiento en x", -2.0, 2.0, 0.5)
        ky = st.slider("Factor de cizallamiento en y", -2.0, 2.0, 0.0)
        T = np.array([
            [1, kx],
            [ky, 1]
        ])
    elif transformacion == "Reflexión":
        reflexion = st.radio("Eje de reflexión:", ["Eje X", "Eje Y", "Recta y=x"])
        if reflexion == "Eje X":
            T = np.array([
                [1, 0],
                [0, -1]
            ])
        elif reflexion == "Eje Y":
            T = np.array([
                [-1, 0],
                [0, 1]
            ])
        else:  # y = x
            T = np.array([
                [0, 1],
                [1, 0]
            ])
    else:  # Personalizada
        st.write("Define tu matriz de transformación:")
        t11 = st.number_input("t₁₁", value=1.0)
        t12 = st.number_input("t₁₂", value=0.0)
        t21 = st.number_input("t₂₁", value=0.0)
        t22 = st.number_input("t₂₂", value=1.0)
        T = np.array([
            [t11, t12],
            [t21, t22]
        ])
    
    # Vector original
    st.subheader("Vector original")
    x = st.slider("Coordenada x del vector", -10.0, 10.0, 2.0)
    y = st.slider("Coordenada y del vector", -10.0, 10.0, 3.0)
    v = np.array([x, y])
    
    # Aplicar transformación
    v_transformado = np.dot(T, v)
    
    # Mostrar resultados
    st.latex(f"T = {T}")
    st.latex(f"\vec{{v}} = {v}")
    st.latex(f"T(\vec{{v}}) = {v_transformado}")
    
    # Visualización
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Vector original
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector original')
    
    # Vector transformado
    ax.quiver(0, 0, v_transformado[0], v_transformado[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector transformado')
    
    # Configuración del gráfico
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.2)
    ax.axvline(x=0, color='k', linestyle='--', alpha=0.2)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    ax.set_title(f"Transformación: {transformacion}")
    st.pyplot(fig)

# Sección de Espacios Vectoriales
elif opcion == "Espacios Vectoriales":
    st.header("🌌 Espacios Vectoriales")
    
    st.subheader("Comprobación de independencia lineal")
    
    st.write("Ingresa tres vectores en R³:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        v1 = np.array([
            st.number_input("v₁₁", value=1.0),
            st.number_input("v₂₁", value=0.0),
            st.number_input("v₃₁", value=0.0)
        ])
    
    with col2:
        v2 = np.array([
            st.number_input("v₁₂", value=0.0),
            st.number_input("v₂₂", value=1.0),
            st.number_input("v₃₂", value=0.0)
        ])
    
    with col3:
        v3 = np.array([
            st.number_input("v₁₃", value=1.0),
            st.number_input("v₂₃", value=1.0),
            st.number_input("v₃₃", value=0.0)
        ])
    
    # Crear matriz con los vectores como columnas
    A = np.column_stack((v1, v2, v3))
    
    # Calcular determinante
    det = np.linalg.det(A)
    
    st.latex(f"A = {A}")
    st.latex(f"det(A) = {det:.4f}")
    
    if abs(det) > 1e-10:
        st.success("Los vectores son linealmente independientes (forman una base para R³)")
    else:
        st.error("Los vectores son linealmente dependientes (no forman una base para R³)")
    
    # Visualización 3D (proyección 2D)
    st.subheader("Visualización de los vectores (proyección 2D)")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Proyección en plano XY
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='g', label='v2')
    ax.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b', label='v3')
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.2)
    ax.axvline(x=0, color='k', linestyle='--', alpha=0.2)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    ax.set_title("Proyección en el plano XY")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("""
**Creado por: Javier Horacio Pérez Ricárdez**            
**Aplicación desarrollada para la enseñanza de Álgebra Lineal**  
*Universidad Tecnológica de Tamaulipas Norte - Departamento de Matemáticas*
""")