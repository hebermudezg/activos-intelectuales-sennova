


-- Inserción en la tabla Usuario
INSERT INTO usuario (id_usuario, nombre_completo, correo_electronico, telefono, rol)
VALUES 
(1, 'Juan Perez', 'juan.perez@example.com', '1234567890', 'Coordinador'),
(2, 'Ana López', 'ana.lopez@example.com', '1234567891', 'Líder'),
(3, 'Carlos Ruiz', 'carlos.ruiz@example.com', '1234567892', 'Miembro'),
(4, 'Maria Gomez', 'maria.gomez@example.com', '1234567893', 'Investigador'),
(5, 'Luis Fernández', 'luis.fernandez@example.com', '1234567894', 'Analista');

-- Inserción en la tabla Producto
INSERT INTO producto (id, categoria, nombre_del_producto, producto_terminado)
VALUES 
(1, 'Libro', 'Introducción a SQL', true),
(2, 'Software', 'Gestor de Proyectos', false),
(3, 'Artículo', 'La evolución de la AI', true),
(4, 'Informe', 'Impacto del COVID-19 en la salud mental', true),
(5, 'Software', 'Plataforma de Telemedicina', true),
(6, 'Artículo', 'Avances en Biotecnología', false);

-- Inserción en la tabla Programa con enfoque en salud
INSERT INTO programa (id, nombre_del_programa, tipo)
VALUES 
(1, 'Programa de Biomedicina', 'Tecnológico'),
(2, 'Programa de Salud Pública', 'Técnico'),
(3, 'Programa de Innovación en Salud', 'Tecnológico'),
(4, 'Programa de Epidemiología', 'Técnico'),
(5, 'Programa de Ingeniería Biomédica', 'Tecnológico');

-- Inserción en la tabla Proyecto
INSERT INTO proyecto (id_proyecto, titulo, fecha_inicio, fecha_fin, entidad_financia, codigo_sgp, valor, linea_programatica, resumen)
VALUES 
(1, 'Desarrollo de Nuevas Protesis', '2023-01-01', '2023-12-31', 'Ministerio de Salud', 'SGP123', 500000, 'Biomedicina', 'Creación y testeo de protesis avanzadas'),
(2, 'Vacunación y Salud Pública', '2023-02-01', '2023-12-31', 'Ministerio de Salud', 'SGP124', 750000, 'Salud Pública', 'Estrategias de vacunación a gran escala'),
(3, 'Telemedicina para Áreas Remotas', '2023-03-01', '2023-12-31', 'Ministerio de Salud', 'SGP125', 600000, 'Telemedicina', 'Desarrollo de soluciones de telemedicina para zonas de difícil acceso'),
(4, 'Investigación en Enfermedades Raras', '2023-04-01', '2024-03-31', 'Ministerio de Salud', 'SGP126', 850000, 'Biomedicina', 'Estudio sobre enfermedades raras y posibles tratamientos'),
(5, 'Plataforma de Gestión Hospitalaria', '2023-05-01', '2024-04-30', 'Ministerio de Salud', 'SGP127', 700000, 'Ingeniería Biomédica', 'Desarrollo de una plataforma avanzada para la gestión hospitalaria');

-- Inserción en la tabla de asociación proyecto_programa para establecer la relación muchos a muchos
INSERT INTO proyecto_programa (proyecto_id, programa_id)
VALUES 
(1, 1),
(1, 5),
(2, 2),
(2, 4),
(3, 3),
(3, 5),
(4, 1),
(4, 4),
(5, 3),
(5, 5);


-- Desactivar las restricciones de clave foránea para evitar errores al eliminar
ALTER TABLE IF EXISTS proyecto_programa DROP CONSTRAINT IF EXISTS proyecto_programa_proyecto_id_fkey;
ALTER TABLE IF EXISTS proyecto_programa DROP CONSTRAINT IF EXISTS proyecto_programa_programa_id_fkey;

-- Eliminar las tablas
DROP TABLE IF EXISTS usuario CASCADE;
DROP TABLE IF EXISTS producto CASCADE;
DROP TABLE IF EXISTS proyecto_programa CASCADE;
DROP TABLE IF EXISTS proyecto CASCADE;
DROP TABLE IF EXISTS programa CASCADE;

-- Consulta para verificar los registros insertados en la tabla Producto
SELECT *
FROM producto;
